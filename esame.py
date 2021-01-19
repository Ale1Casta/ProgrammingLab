class ExamException(Exception):
    pass


class Diff():


    def __init__(self, ratio = 1):
        self.ratio = ratio

        if not isinstance(ratio, int):
            raise ExamException('Invalid type for window, only int supported. Got "{}"'.format(type(ratio)))

        if ratio == 0:
            raise ExamException('Zero ratio value provided')

        self.lungFin = lungFin


    def compute(self, nlist):
        result = []
        lung = len(nlist) - 1

        for i in range(len(nlist)+1):
            
            if i < self.lungFin:
                continue
            else:
                result.append(float((nlist[i+1]-nlist[i])/self.ratio)
                
        return result









   
    diff = Diff()
    result = diff.compute([2,4,8,16])
    print(result)