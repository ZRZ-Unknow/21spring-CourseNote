import os, re
import numpy as np
from functools import reduce
from itertools import product
from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection as HSI
import time

class Game:
    def __init__(self, n_players, actions, payoffs):
        self.n_players = n_players
        self.actions = actions
        self.payoffs = payoffs
    
    def write_nes(self, nes, out_path):
        with open(out_path, 'w') as f:
            for ne in nes:
                to_str = [str(i) if i>1e-15 else '0' for i in ne]
                f.writelines(reduce(lambda x,y:x+','+y, to_str)+'\n')

    def build_pne(self):
        all_best_res = dict()
        for i in range(self.n_players):
            payoff = self.payoffs[i]
            best_res = set()
            for strategy in product(*(range(self.actions[j]) if j!=i else [None] for j in range(self.n_players))):
                subp = [payoff[(*strategy[0:i], j, *strategy[i+1:])] for j in range(self.actions[i])]
                for j in np.argwhere(np.array(subp) == max(subp)):
                    best_res.add((*strategy[0:i], j[0], *strategy[i+1:]))
            all_best_res[i] = best_res
        pnes = set()
        for p in all_best_res[0]:
            if all([p in all_best_res[i] for i in range(1,self.n_players)]):
                pne = [0]*sum(self.actions)
                for j in range(len(p)):
                    pne[p[j] + sum(self.actions[:j])] = 1
                pnes.add(tuple(pne))
        return pnes
    
    def get_pole(self, P):
        A = np.concatenate((P[0], np.linalg.norm(P[0], axis=1, keepdims=True)), axis=1)
        c = np.array([0]*(A.shape[1]-1) + [-1])
        res = linprog(c=c, A_ub=A, b_ub=P[1]).x[:-1]
        hs = HSI(np.concatenate((P[0], -np.expand_dims(P[1], axis=1)), axis=1), res)
        hs.close()
        poles = []
        for v in hs.intersections:
            if np.isfinite(v).all() and (np.abs(v)>1e-8).any():
                label = np.where(np.abs(P[0].dot(v)-P[1])<1e-8)[0]
                poles.append((v, label))
        return poles

    def lp_alg(self):
        'Labeled Polytopes Algorithm'
        payoff0 = self.payoffs[0] + np.abs(np.min(self.payoffs[0])) if (self.payoffs[0]<0).any() else self.payoffs[0]
        payoff1 = self.payoffs[1] + np.abs(np.min(self.payoffs[1])) if (self.payoffs[1]<0).any() else self.payoffs[1]
        A = np.concatenate((payoff0, -np.identity(self.payoffs[0].shape[1])))
        a = np.array([1]*self.actions[0] + [0]*(sum(self.actions) - self.actions[0]))
        B = np.concatenate((payoff1.T, -np.identity(self.payoffs[1].shape[0])))
        b = np.array([1]*self.actions[1] + [0]*(sum(self.actions) - self.actions[1]))
        P1, P2 = [A, a], [B, b]
        nes, label = set(), set(range(sum(self.actions)))
        pole1, pole2 = self.get_pole(P1), self.get_pole(P2)
        for v1, label1 in pole1:
            for v2, label2 in pole2:
                label2 = (label2 + self.actions[0]) % sum(self.actions)
                if set(list(label1)+list(label2)) == label:
                    ne = list(v2/np.sum(v2)) + list(v1/np.sum(v1)) 
                    nes.add(tuple(ne))
        return nes
    
    def find_all_nes(self):
        if self.n_players > 2:
            return self.build_pne()
        else:
            return self.lp_alg()


def read_nfg(filename):
    with open(filename,'r') as f:
        payoffs = []
        pattern = re.compile(r"(?<=\{)[^}]*(?=\})")
        for line in f:
            matched = pattern.findall(line)
            if len(matched) == 2:
                n_player = matched[0].count("Player")
                actions = list(map(lambda x: int(x), matched[1].strip().split()))
                payoff_list = list(map(lambda x: int(x), f.read().strip().split()))
                assert n_player*reduce(lambda x,y:x*y, actions) == len(payoff_list)
                for i in range(n_player):
                    p = [payoff_list[j] for j in range(len(payoff_list)) if j%n_player == i]
                    tmp = np.array([p])
                    tmp = np.reshape(tmp, actions, order='F')
                    payoffs.append(tmp)
                return n_player, actions, payoffs
        assert 0, "should not reach here!"

def gen_game(filename):
    return Game(*read_nfg(filename))

def nash(in_path, out_path):
    time1 = time.time()
    game = gen_game(in_path)
    game.write_nes(game.find_all_nes(), out_path)
    time2 = time.time()
    print(f"Finish {in_path}, Time Used: {time2-time1}")

def run():
    np.random.seed(0)
    if not os.path.exists('./output'):
        os.mkdir('./output')
    for f in os.listdir('input'):
        if f.endswith('.nfg'):
            nash('input/'+f, 'output/'+f.replace('nfg','ne'))


if __name__ == '__main__':
    run()