import argparse
import random
import time
import utils


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        dest='n',
                        type=int,
                        required=True,
                        help='Number of elements in the list')
    parser.add_argument('--num_searches',
                        type=int,
                        required=True,
                        help='Number of queires')
    return parser.parse_args()


def main():
    args = get_args()

    L = random.sample(range(1, args.n*1000), args.n)

    linear_search_total_time = 0
    for i in range(args.num_searches):
        k = random.randint(1, args.n*1000)
        tic = time.perf_counter()
        i = utils. linear_search(L, k)
        toc = time.perf_counter()
        linear_search_total_time += toc - tic

    linear_search_mean_time = linear_search_total_time / args.num_searches
    print('Linear search: '
          + '{:.5f}'.format(linear_search_mean_time)
          + ' seconds')

    tic = time.perf_counter()
    I_idx = utils.index_list(L)
    toc = time.perf_counter()

    bsearch_idx_time = toc - tic

    print('Indexing: '
          + '{:.5f}'.format(bsearch_idx_time)
          + ' seconds')

    bsearch_total_time = 0
    for i in range(args.num_searches):
        k = random.randint(1, args.n*1000)
        tic = time.perf_counter()
        i = utils.binary_search(I_idx, k)
        toc = time.perf_counter()
        bsearch_total_time += toc - tic

    bsearch_mean_time = bsearch_total_time / args.num_searches
    print('Binary search: '
          + '{:.5f}'.format(bsearch_mean_time)
          + ' seconds')


if __name__ == '__main__':
    main()
