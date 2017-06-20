import media
import fresh_tomatoes
secret_superstar=media.Movie("Secret Superstar","A story of Secret Superstar","https://i.ytimg.com/vi/cDFczfMa1VY/maxresdefault.jpg","https://www.youtube.com/watch?v=CNS90MGVCeE")
dhoom4=media.Movie("Dhoom 4","DHOOM 4 Trailer Salman Khan Hrithik Roshan Abhishek Bachchan Uday Chopra fanmade","https://i.ytimg.com/vi/wle7AKVikw8/hqdefault.jpg","https://www.youtube.com/watch?v=2WU1RZGEL0M")
tubelight=media.Movie("TubeLight","Tubelight is an upcoming Indian historical war drama film written, and directed by Kabir Khan","http://static.koimoi.com/wp-content/new-galleries/2017/04/tubelight-poster-2-salman-khan-shoes-dangling-around-neck-1.jpg","https://www.youtube.com/watch?v=PGQRNKHJwH4") 
halfgirlfriend=media.Movie("Half Girlfriend","Half Girlfriend is an Indian romantic drama film based on the novel of the same name written by Chetan Bhagat.","http://www.media.glamsham.com/download/poster/images/half-girlfriend/03-half-girlfriend.jpg","https://www.youtube.com/watch?v=KmlBnmyelHI")
bankchor=media.Movie("Bank Chor","Bank Chor is an upcoming Bollywood film directed by Bumpy and produced by Asish patil.","https://i.ytimg.com/vi/Kx0jZWnlS3Y/hq720.jpg","https://www.youtube.com/watch?v=Kx0jZWnlS3Y")
sachin=media.Movie("Sachin: A Billion Dreams","Sachin: A Billion Dreams is a 2017 Indian docudrama-biographical film directed by James Erskine and produced by Ravi Bhagchandka","http://www.freepressjournal.in/wp-content/uploads/2017/04/Sachin-1.jpg","https://www.youtube.com/watch?v=8gTeE6pa4Kg")
movies=[secret_superstar,dhoom4,tubelight,halfgirlfriend,bankchor,sachin]
fresh_tomatoes.open_movies_page(movies)

