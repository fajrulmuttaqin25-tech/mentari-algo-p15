def shell_sort_nama(arr):
    """
    Mengurutkan list nama menggunakan algoritma Shell Sort
    secara alfabetis (ascending).
    
    Parameter:
        arr (list): List nama (string) yang akan diurutkan.
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].lower() > temp.lower():
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    nama_list = ["Fajrul", "Melani", "Ilyas", "Zikri", "Sayyid", "Eef"]
    
    print("=== Program Pengurutan Nama dengan Shell Sort ===")
    print(f"\nList nama sebelum diurutkan: {nama_list}")
    
    shell_sort_nama(nama_list)
    
    print(f"List nama setelah diurutkan : {nama_list}")