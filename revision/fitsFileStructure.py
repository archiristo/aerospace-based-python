from astropy.io import fits

#fits dosyası açmak
hdul = fits.open('example.fits')

#hdu erişimi
data_hdu = hdul[0]

#veri erişimi
data = data_hdu.data
header = data_hdu.header

print(data, header)

#dosyayı kapat
hdul.close()