def GetFilePath(path):
    lablepath = r"{}".format(path)
    return lablepath


def MakeEmptyFile(emptyFileName):
    fw = open("./labels/{}.txt".format(emptyFileName), 'w')


def MakeFile(file_name, Annotation_tag, left, top, right, bottom, over_count):
    file_name = file_name.split('/')[-1]
    file_name = file_name.split('.')[0]
    print(file_name)
    data = ""
    if over_count > 1:
        fw = open("./labels/{}.txt".format(file_name), 'a')
    else:
        fw = open("./labels/{}.txt".format(file_name), 'w')

    x = (int(left) + int(right)) / 2 / 1280
    y = (int(top) + int(bottom)) / 2 / 960
    w = (int(right) - int(left)) / 1280
    h = (int(bottom) - int(top)) / 960

    if Annotation_tag == 'go':
        ID = 0
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'stop':
        ID = 1
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'stopLeft':
        ID = 2
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'warning':
        ID = 3
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'goLeft':
        ID = 4
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'warningLeft':
        ID = 5
        data += f"{ID} {x} {y} {w} {h}\n"
    elif Annotation_tag == 'goForward':
        ID = 6
        data += f"{ID} {x} {y} {w} {h}\n"
    else:
        data += ""

    if over_count > 1:
        fw.write(data)
        fw.close()
    else:
        fw.write(data)
        fw.close()


def TransForm(labels):
    last_index_count = 0
    over_count = 1
    index = 0

    fr = open(labels, 'r')
    text = fr.readlines()
    text_len = int(text[-1].split(';')[-1]) + 1
    for count in range(text_len):
        emptyFileName = labels.split('/')[-2]
        emptyFileName += "--" + str(count).zfill(5)
        while True:
            file_name, Annotation_tag, left, top, right, bottom = text[index].split(';')[0:6]
            text_index = int(text[index].split(';')[-1])
            # 이미지 인덱스와 csv 인덱스가 같고 같은 csv 인덱스가 반복된다면 파일을 덮어 씌우고 1출 추가
            if count == text_index and last_index_count == count:
                last_index_count = count
                MakeFile(file_name, Annotation_tag, left, top, right, bottom, over_count)
                over_count += 1

            # 이미지 인덱스와 csv 인덱스가 같고 같은 처음만난 csv 인덱스 파일을 생성
            elif count == text_index and last_index_count != count:
                last_index_count = count
                MakeFile(file_name, Annotation_tag, left, top, right, bottom, over_count)
                over_count += 1

            # 이미지 인덱스와 csv 인덱스가 같지 않으면 빈 txt파일을 이미지 파일 인덱스 이름으로 생성
            elif count != text_index and last_index_count != count:
                last_index_count = count
                over_count = 1
                MakeEmptyFile(emptyFileName)
                print(emptyFileName)
                break

            # 이미지 인덱스와 csv 인덱스가 같지 않고 같은 파일이 반복되는 경우
            else:
                last_index_count = count
                over_count = 1
                break
            if index < len(text) - 1:
                index += 1
            else:
                break


if __name__ == '__main__':
    # DayTrainData
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip1/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip2/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip3/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip4/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip5/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/sample-dayClip6/sample-dayClip6/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip7/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip8/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip9/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip10/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip11/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip12/frameAnnotationsBOX.csv')
    TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/dayTrain/dayClip13/frameAnnotationsBOX.csv')

    # DayValData
    # TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/daySequence1/frameAnnotationsBOX.csv')
    # TransForm('C:/Users/user/Desktop/archive/Annotations/Annotations/daySequence2/frameAnnotationsBOX.csv')
