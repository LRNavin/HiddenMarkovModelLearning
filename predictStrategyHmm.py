import sys

from main import main

if __name__ == "__main__":

    test_log = str(sys.argv[1])

    main = main()
    main.run_hmm_prediction(test_log)