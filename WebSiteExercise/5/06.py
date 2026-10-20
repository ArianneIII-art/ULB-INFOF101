def transcription_arn(brin_codant):
    for i in range(len(brin_codant)):
        if brin_codant[i] == "T":
            brin_codant = brin_codant[:i] + "U" + brin_codant[i+1:] 
    return brin_codant