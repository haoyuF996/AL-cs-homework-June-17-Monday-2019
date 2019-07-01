def merge_sort(alist):
    '''Merge sort,return sorted list'''
    if len(alist)>2:
        l = merge_sort(alist[:len(alist)//2])
        r = merge_sort(alist[len(alist)//2:])
        product = []
        while r!=[] and l!=[]:
            if r[0]>l[0]:
                product.append(l[0])
                del l[0]
            else:
                product.append(r[0])
                del r[0]
        if r == []:
            product.extend(l)
        else:
            product.extend(r)
        return product
    if len(alist)==2:
        if alist[0]>alist[1]:
            alist[0],alist[1] = alist[1],alist[0]
        return alist
    else:
        return alist