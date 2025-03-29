from consts import DATADIR, NAME, SUBSET
from datasets import load_from_disk

if __name__ == "__main__":
    train_ds = load_from_disk(f'{DATADIR}/{NAME}-{SUBSET}-train')
    print(train_ds[0])