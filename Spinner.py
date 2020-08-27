def counterClockwise(data): #membuat function untuk merubah list menjadi counter clockwise
    temp1 = data[0][0] #membuat temp 1 untuk memindahkan index ke 0 ke index 2 ke 0
    data[0][0]=data[2][0]
    data[2][0]=temp1 
    
    temp2 = data[0][1] #membuat temp 2 untuk memindahkan index ke 0,1 ke index 1 ke 0
    data[0][1]=data[1][0]
    data[1][0]=temp2
    
    
    temp3 = data[0][2] #membuat temp 3 untuk memindahkan index ke 0,2 ke index 0 ke 0
    data[0][2]=data[0][0]            
    data[0][0]=temp3  
    
    temp4 = data[2][1] #membuat temp 4 agar angka 8 tidak berubah posisinya
    data[2][1]=data[2][2]
    data[2][1]=temp4
    
    temp5 = data[1][2] #temp5 memindahkan angka 6 ke index 0,1
    data[1][2]=data[0][1]
    data[0][1]=temp5
    
    temp6 = data[2][0]#temp6 memastikan angka 1 tetap ditempat
    data[2][0]=data[2][0]
    data[2][0]=temp6
    
    temp7 = data[2][1] #temp7 memindahkan angka 8 ke index 1,2
    data[2][1]=data[1][2]
    data[1][2]=temp7
    
    
    temp8 = data[2][2] #temp8 menukarkan angka 7 yang ada diindex ke 2,2 menjadi angka 9 yang adad di 2,2 dan angka 7 ada di 0,2
    data[2][2]=data[0][2]
    data[0][2]=temp8
    
    return data
    
data=[[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(counterClockwise(data))