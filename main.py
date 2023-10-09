import matplotlib.pyplot as plt
import networkx as nx
import random as random
import heapq
import math

import time
import maze, utilities, a_star, v1, v2, v3

import memory_profiler as mem_profile

if __name__ == "__main__":
    # print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))
    mem_before = mem_profile.memory_usage()
    columns = 65


    # rows = int(columns/2)
    [g, start, end] = maze.create_maze(columns)

    maze.draw_maze(g, start,end, [])
    # mem_before = mem_profile.memory_usage()
    # # a -> a *
    # time_start = time.time()
    [d_a, cost_a] = a_star.a_star_search(
        g, start, end
    )
    path_a =  utilities.get_path(d_a,end)
    # mem_a = mem_profile.memory_usage()
    # time_a = time.time()
    # # vwa1 -> variable weighted a * v1

    # [d_vwa1, cost_vwa1] = v1.vw_a_star_1(
    #     g, start, end
    # )
    # path_vwa1=  utilities.get_path(d_vwa1,end)
    # mem_1 = mem_profile.memory_usage()
    # time_1 = time.time()
    # # vwa2 -> variable weighted a * v2
    # [d_vwa2, cost_vwa2] = v2.vw_a_star_2(
    #     g, start, end
    # )
    # # path_vwa2=  utilities.get_path(d_vwa2,end)
    # mem_2 = mem_profile.memory_usage()
    # time_2 = time.time()
    # # vwa3 -> variable weighted a * v3
    # [d_vwa3, cost_vwa3] = v3.vw_a_star_3(
    #     g, start, end
    # )
    # # path_vwa3=  utilities.get_path(d_vwa3,end)
    # mem_3 = mem_profile.memory_usage()
    # time_3 = time.time()
    # print(
    #     f"{time_a-time_start},{(mem_a[0]-mem_before[0]):.15f}"
    # )

    # print(f"Time A*: {time_a-time_start}")
    # print(
    #     f"Memory usage of A*: {(mem_a[0]-mem_before[0]):.15f} MB"
    # )
    # print(
    #     f"{time_1-time_a},{(mem_1[0]-mem_a[0]):.15f}"
    # )
    # # print(f"Time VWA* 1: {time_1-time_a}")
    # # print(
    # #     f"Memory usage of VWA* Ver. 1: {(mem_1[0]-mem_a[0]):.15f} MB"
    # # )
    # print(
    #     f"{time_2-time_1},{(mem_2[0]-mem_1[0]):.15f}"
    # )
    # # print(f"Time VWA* 2: {time_2-time_1}")
    # # print(
    # #     f"Memory usage of VWA* Ver. 2: {(mem_2[0]-mem_1[0]):.15f} MB"
    # # )
    # print(
    #     f"{time_3-time_2},{(mem_3[0]-mem_2[0]):.15f}"
    # )
    # print(f"Time VWA* 3: {time_3-time_2}")
    # print(
    #     f"Memory usage of VWA* Ver. 3: {(mem_3[0]-mem_2[0]):.15f} MB"
    # )
    maze.draw_maze(g,start,end, path_a)
