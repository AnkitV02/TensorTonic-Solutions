import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len==None:
        max_len = max([len(seq) for seq in seqs]) or 0
    ans=[]
    for seq in seqs:
        if len(seq)>max_len:
            ans.append(seq[:max_len])

        elif len(seq)<max_len:
            for _ in range(max_len-len(seq)):
                seq.append(pad_value)

            ans.append(seq)

        else:
            ans.append(seq)


    return ans
            

    
        