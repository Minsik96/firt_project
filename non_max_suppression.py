import numpy as np


def non_maxium_suppression(boxes, probs, overlap_theshold):

    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]

    area = (x2 - x1) * (y2 - y1) + 1 # 결과에 무관하도록 상수 1을 더함

    while len(probs) > 0 :
        idxs = np.argsort(probs)
        last = lend(idx) - 1
        max_prob_index = idx[last]

        pick = []
        pick.append(max_prob_index)

        xx1 = np.maximum(x1[max_prob_index], x1[idxs[:last]])
        yy1 = np.maximum(y1[max_prob_index], y1[idxs[:last]])
        xx2 = np.minimum(x2[max_prob_index], x2[idxs[:last]])
        yy2 = np.minimum(y2[max_prob_index], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        over_lap = (w * h) / area[idxs[:last]]

        idxs = np.delete(idxs , np.concatenate(([last], \
            np.where(over_lap > overlap_theshold[0]))))
        
    return boxes[pick].astype("int")






      