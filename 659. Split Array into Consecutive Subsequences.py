

//
// How to solve?
//
// (e.g.) create sequence from (3,4,5,6,7), (5,6,7), (6,7,8,9,10)
//
//        -> 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10
//
//        visually we are solving
//
//                    *  *
//                 *  *  *
//           *  *  *  *  *  *  *  *
//           3  4  5  6  7  8  9  10
//
// we are creating open ended sequence as scanning through 3 to 10
//
// At 3, there is no open sequence so [3) will be created
//
// At 4, #(4) == #(open sequence)
//   so don't close the open sequences, just extends them
//    [3 4)
//
// At 5, #(5) > #(open sequences)  : (2 > 1)
//   so we extends existing open sequences, plus new sequence from '5'
//     [3 4 5)
//         [5)
//
// At 6, same situation as at '5',
//     [3 4 5 6)
//         [5 6)
//           [6)
//
// At 7, same as at 4 #(7) == #(seq)
//
//     [3 4 5 6 7)
//         [5 6 7)
//           [6 7)
//
// At 8, #(8) < #(seq) so we must close sequences if we can
//   (if not return false)
//
//     [3 4 5 6 7] --> done
//         [5 6 7] --> done
//           [6 7 8)
//
// At 9 and 10, we are just extending sequences
//           [6 7 8 9 10)
//
// At the end, if we can close all open sequences, return 'true'
// If not return 'false'
//
              
              
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ncount = dict()
        for num in nums:
            if num not in ncount:
                ncount[num] = 0
            ncount[num] += 1
            
        sequences = []
        for num in sorted(ncount.keys()):
            count = ncount[num]
            s = len(sequences)-1
            for _ in range(count):
                if s>= 0 and sequences[s][-1] + 1 == num:
                    sequences[s].append(num)
                    s -= 1
                else:
                    sequences.append([num])
                        
        for sequence in sequences:
            if len(sequence) < 3:
                return False
            
        return True              
