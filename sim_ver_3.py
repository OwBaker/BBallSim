'''
The Third Version of Owen's Basketball Sim, meant to be faster to develop and simpler.
'''

import random as rand
import json

names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley", "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun", "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan", "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz", "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee", "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody", "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan", "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "Caiden-Paul", "Caidyn", "Caie", "Cailaen", "Cailean", "Caileb-John", "Cailin", "Cain", "Caine", "Cairn", "Cal", "Calan", "Calder", "Cale", "Calean", "Caleb", "Calen", "Caley", "Calib", "Calin", "Callahan", "Callan", "Callan-Adam", "Calley", "Callie", "Callin", "Callum", "Callun", "Callyn", "Calum", "Calum-James", "Calvin", "Cambell", "Camerin", "Cameron", "Campbel", "Campbell", "Camron", "Caolain", "Caolan", "Carl", "Carlo", "Carlos", "Carrich", "Carrick", "Carson", "Carter", "Carwyn", "Casey", "Casper", "Cassy", "Cathal", "Cator", "Cavan", "Cayden", "Cayden-Robert", "Cayden-Tiamo", "Ceejay", "Ceilan", "Ceiran", "Ceirin", "Ceiron", "Cejay", "Celik", "Cephas", "Cesar", "Cesare", "Chad", "Chaitanya", "Chang-Ha", "Charles", "Charley", "Charlie", "Charly", "Chase", "Che", "Chester", "Chevy", "Chi", "Chibudom", "Chidera", "Chimsom", "Chin", "Chintu", "Chiqal", "Chiron", "Chris", "Chris-Daniel", "Chrismedi", "Christian", "Christie", "Christoph", "Christopher", "Christopher-Lee", "Christy", "Chu", "Chukwuemeka", "Cian", "Ciann", "Ciar", "Ciaran", "Ciarian", "Cieran", "Cillian", "Cillin", "Cinar", "CJ", "C-Jay", "Clark", "Clarke", "Clayton", "Clement", "Clifford", "Clyde", "Cobain", "Coban", "Coben", "Cobi", "Cobie", "Coby", "Codey", "Codi", "Codie", "Cody", "Cody-Lee", "Coel", "Cohan", "Cohen", "Colby", "Cole", "Colin", "Coll", "Colm", "Colt", "Colton", "Colum", "Colvin", "Comghan", "Conal", "Conall", "Conan", "Conar", "Conghaile", "Conlan", "Conley", "Conli", "Conlin", "Conlly", "Conlon", "Conlyn", "Connal", "Connall", "Connan", "Connar", "Connel", "Connell", "Conner", "Connolly", "Connor", "Connor-David", "Conor", "Conrad", "Cooper", "Copeland", "Coray", "Corben", "Corbin", "Corey", "Corey-James", "Corey-Jay", "Cori", "Corie", "Corin", "Cormac", "Cormack", "Cormak", "Corran", "Corrie", "Cory", "Cosmo", "Coupar", "Craig", "Craig-James", "Crawford", "Creag", "Crispin", "Cristian", "Crombie", "Cruiz", "Cruz", "Cuillin", "Cullen", "Cullin", "Curtis", "Cyrus", "Daanyaal", "Daegan", "Daegyu", "Dafydd", "Dagon", "Dailey", "Daimhin", "Daithi", "Dakota", "Daksh", "Dale", "Dalong", "Dalton", "Damian", "Damien", "Damon", "Dan", "Danar", "Dane", "Danial", "Daniel", "Daniele", "Daniel-James", "Daniels", "Daniil", "Danish", "Daniyal", "Danniel", "Danny", "Dante", "Danyal", "Danyil", "Danys", "Daood", "Dara", "Darach", "Daragh", "Darcy", "D'arcy", "Dareh", "Daren", "Darien", "Darius", "Darl", "Darn", "Darrach", "Darragh", "Darrel", "Darrell", "Darren", "Darrie", "Darrius", "Darroch", "Darryl", "Darryn", "Darwyn", "Daryl", "Daryn", "Daud", "Daumantas", "Davi", "David", "David-Jay", "David-Lee", "Davie", "Davis", "Davy", "Dawid", "Dawson", "Dawud", "Dayem", "Daymian", "Deacon", "Deagan", "Dean", "Deano", "Decklan", "Declain", "Declan", "Declyan", "Declyn", "Dedeniseoluwa", "Deecan", "Deegan", "Deelan", "Deklain-Jaimes", "Del", "Demetrius", "Denis", "Deniss", "Dennan", "Dennin", "Dennis", "Denny", "Dennys", "Denon", "Denton", "Denver", "Denzel", "Deon", "Derek", "Derick", "Derin", "Dermot", "Derren", "Derrie", "Derrin", "Derron", "Derry", "Derryn", "Deryn", "Deshawn", "Desmond", "Dev", "Devan", "Devin", "Devlin", "Devlyn", "Devon", "Devrin", "Devyn", "Dex", "Dexter", "Dhani", "Dharam", "Dhavid", "Dhyia", "Diarmaid", "Diarmid", "Diarmuid", "Didier", "Diego", "Diesel", "Diesil", "Digby", "Dilan", "Dilano", "Dillan", "Dillon", "Dilraj", "Dimitri", "Dinaras", "Dion", "Dissanayake", "Dmitri", "Doire", "Dolan", "Domanic", "Domenico", "Domhnall", "Dominic", "Dominick", "Dominik", "Donald", "Donnacha", "Donnie", "Dorian", "Dougal", "Douglas", "Dougray", "Drakeo", "Dre", "Dregan", "Drew", "Dugald", "Duncan", "Duriel", "Dustin", "Dylan", "Dylan-Jack", "Dylan-James", "Dylan-John", "Dylan-Patrick", "Dylin", "Dyllan", "Dyllan-James", "Dyllon", "Eadie", "Eagann", "Eamon", "Eamonn", "Eason", "Eassan", "Easton", "Ebow", "Ed", "Eddie", "Eden", "Ediomi", "Edison", "Eduardo", "Eduards", "Edward", "Edwin", "Edwyn", "Eesa", "Efan", "Efe", "Ege", "Ehsan", "Ehsen", "Eiddon", "Eidhan", "Eihli", "Eimantas", "Eisa", "Eli", "Elias", "Elijah", "Eliot", "Elisau", "Eljay", "Eljon", "Elliot", "Elliott", "Ellis", "Ellisandro", "Elshan", "Elvin", "Elyan", "Emanuel", "Emerson", "Emil", "Emile", "Emir", "Emlyn", "Emmanuel", "Emmet", "Eng", "Eniola", "Enis", "Ennis", "Enrico", "Enrique", "Enzo", "Eoghain", "Eoghan", "Eoin", "Eonan", "Erdehan", "Eren", "Erencem", "Eric", "Ericlee", "Erik", "Eriz", "Ernie-Jacks", "Eroni", "Eryk", "Eshan", "Essa", "Esteban", "Ethan", "Etienne", "Etinosa", "Euan", "Eugene", "Evan", "Evann", "Ewan", "Ewen", "Ewing", "Exodi", "Ezekiel", "Ezra", "Fabian", "Fahad", "Faheem", "Faisal", "Faizaan", "Famara", "Fares", "Farhaan", "Farhan", "Farren", "Farzad", "Fauzaan", "Favour", "Fawaz", "Fawkes", "Faysal", "Fearghus", "Feden", "Felix", "Fergal", "Fergie", "Fergus", "Ferre", "Fezaan", "Fiachra", "Fikret", "Filip", "Filippo", "Finan", "Findlay", "Findlay-James", "Findlie", "Finlay", "Finley", "Finn", "Finnan", "Finnean", "Finnen", "Finnlay", "Finnley", "Fintan", "Fionn", "Firaaz", "Fletcher", "Flint", "Florin", "Flyn", "Flynn", "Fodeba", "Folarinwa", "Forbes", "Forgan", "Forrest", "Fox", "Francesco", "Francis", "Francisco", "Franciszek", "Franco", "Frank", "Frankie", "Franklin", "Franko", "Fraser", "Frazer", "Fred", "Freddie", "Frederick", "Fruin", "Fyfe", "Fyn", "Fynlay", "Fynn", "Gabriel", "Gallagher", "Gareth", "Garren", "Garrett", "Garry", "Gary", "Gavin", "Gavin-Lee", "Gene", "Geoff", "Geoffrey", "Geomer", "Geordan", "Geordie", "George", "Georgia", "Georgy", "Gerard", "Ghyll", "Giacomo", "Gian", "Giancarlo", "Gianluca", "Gianmarco", "Gideon", "Gil", "Gio", "Girijan", "Girius", "Gjan", "Glascott", "Glen", "Glenn", "Gordon", "Grady", "Graeme", "Graham", "Grahame", "Grant", "Grayson", "Greg", "Gregor", "Gregory", "Greig", "Griffin", "Griffyn", "Grzegorz", "Guang", "Guerin", "Guillaume", "Gurardass", "Gurdeep", "Gursees", "Gurthar", "Gurveer", "Gurwinder", "Gus", "Gustav", "Guthrie", "Guy", "Gytis", "Habeeb", "Hadji", "Hadyn", "Hagun", "Haiden", "Haider", "Hamad", "Hamid", "Hamish", "Hamza", "Hamzah", "Han", "Hansen", "Hao", "Hareem", "Hari", "Harikrishna", "Haris", "Harish", "Harjeevan", "Harjyot", "Harlee", "Harleigh", "Harley", "Harman", "Harnek", "Harold", "Haroon", "Harper", "Harri", "Harrington", "Harris", "Harrison", "Harry", "Harvey", "Harvie", "Harvinder", "Hasan", "Haseeb", "Hashem", "Hashim", "Hassan", "Hassanali", "Hately", "Havila", "Hayden", "Haydn", "Haydon", "Haydyn", "Hcen", "Hector", "Heddle", "Heidar", "Heini", "Hendri", "Henri", "Henry", "Herbert", "Heyden", "Hiro", "Hirvaansh", "Hishaam", "Hogan", "Honey", "Hong", "Hope", "Hopkin", "Hosea", "Howard", "Howie", "Hristomir", "Hubert", "Hugh", "Hugo", "Humza", "Hunter", "Husnain", "Hussain", "Hussan", "Hussnain", "Hussnan", "Hyden", "I", "Iagan", "Iain", "Ian", "Ibraheem", "Ibrahim", "Idahosa", "Idrees", "Idris", "Iestyn", "Ieuan", "Igor", "Ihtisham", "Ijay", "Ikechukwu", "Ikemsinachukwu", "Ilyaas", "Ilyas", "Iman", "Immanuel", "Inan", "Indy", "Ines", "Innes", "Ioannis", "Ireayomide", "Ireoluwa", "Irvin", "Irvine", "Isa", "Isaa", "Isaac", "Isaiah", "Isak", "Isher", "Ishwar", "Isimeli", "Isira", "Ismaeel", "Ismail", "Israel", "Issiaka", "Ivan", "Ivar", "Izaak", "J", "Jaay", "Jac", "Jace", "Jack", "Jacki", "Jackie", "Jack-James", "Jackson", "Jacky", "Jacob", "Jacques", "Jad", "Jaden", "Jadon", "Jadyn", "Jae", "Jagat", "Jago", "Jaheim", "Jahid", "Jahy", "Jai", "Jaida", "Jaiden", "Jaidyn", "Jaii", "Jaime", "Jai-Rajaram", "Jaise", "Jak", "Jake", "Jakey", "Jakob", "Jaksyn", "Jakub", "Jamaal", "Jamal", "Jameel", "Jameil", "James", "James-Paul", "Jamey", "Jamie", "Jan", "Jaosha", "Jardine", "Jared", "Jarell", "Jarl", "Jarno", "Jarred", "Jarvi", "Jasey-Jay", "Jasim", "Jaskaran", "Jason", "Jasper", "Jaxon", "Jaxson", "Jay", "Jaydan", "Jayden", "Jayden-James", "Jayden-Lee", "Jayden-Paul", "Jayden-Thomas", "Jaydn", "Jaydon", "Jaydyn", "Jayhan", "Jay-Jay", "Jayke", "Jaymie", "Jayse", "Jayson", "Jaz", "Jazeb", "Jazib", "Jazz", "Jean", "Jean-Lewis", "Jean-Pierre", "Jebadiah", "Jed", "Jedd", "Jedidiah", "Jeemie", "Jeevan", "Jeffrey", "Jensen", "Jenson", "Jensyn", "Jeremy", "Jerome", "Jeronimo", "Jerrick", "Jerry", "Jesse", "Jesuseun", "Jeswin", "Jevan", "Jeyun", "Jez", "Jia", "Jian", "Jiao", "Jimmy", "Jincheng", "JJ", "Joaquin", "Joash", "Jock", "Jody", "Joe", "Joeddy", "Joel", "Joey", "Joey-Jack", "Johann", "Johannes", "Johansson", "John", "Johnathan", "Johndean", "Johnjay", "John-Michael", "Johnnie", "Johnny", "Johnpaul", "John-Paul", "John-Scott", "Johnson", "Jole", "Jomuel", "Jon", "Jonah", "Jonatan", "Jonathan", "Jonathon", "Jonny", "Jonothan", "Jon-Paul", "Jonson", "Joojo", "Jordan", "Jordi", "Jordon", "Jordy", "Jordyn", "Jorge", "Joris", "Jorryn", "Josan", "Josef", "Joseph", "Josese", "Josh", "Joshiah", "Joshua", "Josiah", "Joss", "Jostelle", "Joynul", "Juan", "Jubin", "Judah", "Jude", "Jules", "Julian", "Julien", "Jun", "Junior", "Jura", "Justan", "Justin", "Justinas", "Kaan", "Kabeer", "Kabir", "Kacey", "Kacper", "Kade", "Kaden", "Kadin", "Kadyn", "Kaeden", "Kael", "Kaelan", "Kaelin", "Kaelum", "Kai", "Kaid", "Kaidan", "Kaiden", "Kaidinn", "Kaidyn", "Kaileb", "Kailin", "Kain", "Kaine", "Kainin", "Kainui", "Kairn", "Kaison", "Kaiwen", "Kajally", "Kajetan", "Kalani", "Kale", "Kaleb", "Kaleem", "Kal-el", "Kalen", "Kalin", "Kallan", "Kallin", "Kalum", "Kalvin", "Kalvyn", "Kameron", "Kames", "Kamil", "Kamran", "Kamron", "Kane", "Karam", "Karamvir", "Karandeep", "Kareem", "Karim", "Karimas", "Karl", "Karol", "Karson", "Karsyn", "Karthikeya", "Kasey", "Kash", "Kashif", "Kasim", "Kasper", "Kasra", "Kavin", "Kayam", "Kaydan", "Kayden", "Kaydin", "Kaydn", "Kaydyn", "Kaydyne", "Kayleb", "Kaylem", "Kaylum", "Kayne", "Kaywan", "Kealan", "Kealon", "Kean", "Keane", "Kearney", "Keatin", "Keaton", "Keavan", "Keayn", "Kedrick", "Keegan", "Keelan", "Keelin", "Keeman", "Keenan", "Keenan-Lee", "Keeton", "Kehinde", "Keigan", "Keilan", "Keir", "Keiran", "Keiren", "Keiron", "Keiryn", "Keison", "Keith", "Keivlin", "Kelam", "Kelan", "Kellan", "Kellen", "Kelso", "Kelum", "Kelvan", "Kelvin", "Ken", "Kenan", "Kendall", "Kendyn", "Kenlin", "Kenneth", "Kensey", "Kenton", "Kenyon", "Kenzeigh", "Kenzi", "Kenzie", "Kenzo", "Kenzy", "Keo", "Ker", "Kern", "Kerr", "Kevan", "Kevin", "Kevyn", "Kez", "Khai", "Khalan", "Khaleel", "Khaya", "Khevien", "Khizar", "Khizer", "Kia", "Kian", "Kian-James", "Kiaran", "Kiarash", "Kie", "Kiefer", "Kiegan", "Kienan", "Kier", "Kieran", "Kieran-Scott", "Kieren", "Kierin", "Kiern", "Kieron", "Kieryn", "Kile", "Killian", "Kimi", "Kingston", "Kinneil", "Kinnon", "Kinsey", "Kiran", "Kirk", "Kirwin", "Kit", "Kiya", "Kiyonari", "Kjae", "Klein", "Klevis", "Kobe", "Kobi", "Koby", "Koddi", "Koden", "Kodi", "Kodie", "Kody", "Kofi", "Kogan", "Kohen", "Kole", "Konan", "Konar", "Konnor", "Konrad", "Koray", "Korben", "Korbyn", "Korey", "Kori", "Korrin", "Kory", "Koushik", "Kris", "Krish", "Krishan", "Kriss", "Kristian", "Kristin", "Kristofer", "Kristoffer", "Kristopher", "Kruz", "Krzysiek", "Krzysztof", "Ksawery", "Ksawier", "Kuba", "Kurt", "Kurtis", "Kurtis-Jae", "Kyaan", "Kyan", "Kyde", "Kyden", "Kye", "Kyel", "Kyhran", "Kyie", "Kylan", "Kylar", "Kyle", "Kyle-Derek", "Kylian", "Kym", "Kynan", "Kyral", "Kyran", "Kyren", "Kyrillos", "Kyro", "Kyron", "Kyrran", "Lachlainn", "Lachlan", "Lachlann", "Lael", "Lagan", "Laird", "Laison", "Lakshya", "Lance", "Lancelot", "Landon", "Lang", "Lasse", "Latif", "Lauchlan", "Lauchlin", "Laughlan", "Lauren", "Laurence", "Laurie", "Lawlyn", "Lawrence", "Lawrie", "Lawson", "Layne", "Layton", "Lee", "Leigh", "Leigham", "Leighton", "Leilan", "Leiten", "Leithen", "Leland", "Lenin", "Lennan", "Lennen", "Lennex", "Lennon", "Lennox", "Lenny", "Leno", "Lenon", "Lenyn", "Leo", "Leon", "Leonard", "Leonardas", "Leonardo", "Lepeng", "Leroy", "Leven", "Levi", "Levon", "Levy", "Lewie", "Lewin", "Lewis", "Lex", "Leydon", "Leyland", "Leylann", "Leyton", "Liall", "Liam", "Liam-Stephen", "Limo", "Lincoln", "Lincoln-John", "Lincon", "Linden", "Linton", "Lionel", "Lisandro", "Litrell", "Liyonela-Elam", "LLeyton", "Lliam", "Lloyd", "Lloyde", "Loche", "Lochlan", "Lochlann", "Lochlan-Oliver", "Lock", "Lockey", "Logan", "Logann", "Logan-Rhys", "Loghan", "Lokesh", "Loki", "Lomond", "Lorcan", "Lorenz", "Lorenzo", "Lorne", "Loudon", "Loui", "Louie", "Louis", "Loukas", "Lovell", "Luc", "Luca", "Lucais", "Lucas", "Lucca", "Lucian", "Luciano", "Lucien", "Lucus", "Luic", "Luis", "Luk", "Luka", "Lukas", "Lukasz", "Luke", "Lukmaan", "Luqman", "Lyall", "Lyle", "Lyndsay", "Lysander", "Maanav", "Maaz", "Mac", "Macallum", "Macaulay", "Macauley", "Macaully", "Machlan", "Maciej", "Mack", "Mackenzie", "Mackenzy", "Mackie", "Macsen", "Macy", "Madaki", "Maddison", "Maddox", "Madison", "Madison-Jake", "Madox", "Mael", "Magnus", "Mahan", "Mahdi", "Mahmoud", "Maias", "Maison", "Maisum", "Maitlind", "Majid", "Makensie", "Makenzie", "Makin", "Maksim", "Maksymilian", "Malachai", "Malachi", "Malachy", "Malakai", "Malakhy", "Malcolm", "Malik", "Malikye", "Malo", "Ma'moon", "Manas", "Maneet", "Manmohan", "Manolo", "Manson", "Mantej", "Manuel", "Manus", "Marc", "Marc-Anthony", "Marcel", "Marcello", "Marcin", "Marco", "Marcos", "Marcous", "Marcquis", "Marcus", "Mario", "Marios", "Marius", "Mark", "Marko", "Markus", "Marley", "Marlin", "Marlon", "Maros", "Marshall", "Martin", "Marty", "Martyn", "Marvellous", "Marvin", "Marwan", "Maryk", "Marzuq", "Mashhood", "Mason", "Mason-Jay", "Masood", "Masson", "Matas", "Matej", "Mateusz", "Mathew", "Mathias", "Mathu", "Mathuyan", "Mati", "Matt", "Matteo", "Matthew", "Matthew-William", "Matthias", "Max", "Maxim", "Maximilian", "Maximillian", "Maximus", "Maxwell", "Maxx", "Mayeul", "Mayson", "Mazin", "Mcbride", "McCaulley", "McKade", "McKauley", "McKay", "McKenzie", "McLay", "Meftah", "Mehmet", "Mehraz", "Meko", "Melville", "Meshach", "Meyzhward", "Micah", "Michael", "Michael-Alexander", "Michael-James", "Michal", "Michat", "Micheal", "Michee", "Mickey", "Miguel", "Mika", "Mikael", "Mikee", "Mikey", "Mikhail", "Mikolaj", "Miles", "Millar", "Miller", "Milo", "Milos", "Milosz", "Mir", "Mirza", "Mitch", "Mitchel", "Mitchell", "Moad", "Moayd", "Mobeen", "Modoulamin", "Modu", "Mohamad", "Mohamed", "Mohammad", "Mohammad-Bilal", "Mohammed", "Mohanad", "Mohd", "Momin", "Momooreoluwa", "Montague", "Montgomery", "Monty", "Moore", "Moosa", "Moray", "Morgan", "Morgyn", "Morris", "Morton", "Moshy", "Motade", "Moyes", "Msughter", "Mueez", "Muhamadjavad", "Muhammad", "Muhammed", "Muhsin", "Muir", "Munachi", "Muneeb", "Mungo", "Munir", "Munmair", "Munro", "Murdo", "Murray", "Murrough", "Murry", "Musa", "Musse", "Mustafa", "Mustapha", "Muzammil", "Muzzammil", "Mykie", "Myles", "Mylo", "Nabeel", "Nadeem", "Nader", "Nagib", "Naif", "Nairn", "Narvic", "Nash", "Nasser", "Nassir", "Natan", "Nate", "Nathan", "Nathanael", "Nathanial", "Nathaniel", "Nathan-Rae", "Nawfal", "Nayan", "Neco", "Neil", "Nelson", "Neo", "Neshawn", "Nevan", "Nevin", "Ngonidzashe", "Nial", "Niall", "Nicholas", "Nick", "Nickhill", "Nicki", "Nickson", "Nicky", "Nico", "Nicodemus", "Nicol", "Nicolae", "Nicolas", "Nidhish", "Nihaal", "Nihal", "Nikash", "Nikhil", "Niki", "Nikita", "Nikodem", "Nikolai", "Nikos", "Nilav", "Niraj", "Niro", "Niven", "Noah", "Noel", "Nolan", "Noor", "Norman", "Norrie", "Nuada", "Nyah", "Oakley", "Oban", "Obieluem", "Obosa", "Odhran", "Odin", "Odynn", "Ogheneochuko", "Ogheneruno", "Ohran", "Oilibhear", "Oisin", "Ojima-Ojo", "Okeoghene", "Olaf", "Ola-Oluwa", "Olaoluwapolorimi", "Ole", "Olie", "Oliver", "Olivier", "Oliwier", "Ollie", "Olurotimi", "Oluwadamilare", "Oluwadamiloju", "Oluwafemi", "Oluwafikunayomi", "Oluwalayomi", "Oluwatobiloba", "Oluwatoni", "Omar", "Omri", "Oran", "Orin", "Orlando", "Orley", "Orran", "Orrick", "Orrin", "Orson", "Oryn", "Oscar", "Osesenagha", "Oskar", "Ossian", "Oswald", "Otto", "Owain", "Owais", "Owen", "Owyn", "Oz", "Ozzy", "Pablo", "Pacey", "Padraig", "Paolo", "Pardeepraj", "Parkash", "Parker", "Pascoe", "Pasquale", "Patrick", "Patrick-John", "Patrikas", "Patryk", "Paul", "Pavit", "Pawel", "Pawlo", "Pearce", "Pearse", "Pearsen", "Pedram", "Pedro", "Peirce", "Peiyan", "Pele", "Peni", "Peregrine", "Peter", "Phani", "Philip", "Philippos", "Phinehas", "Phoenix", "Phoevos", "Pierce", "Pierre-Antoine", "Pieter", "Pietro", "Piotr", "Porter", "Prabhjoit", "Prabodhan", "Praise", "Pranav", "Pravin", "Precious", "Prentice", "Presley", "Preston", "Preston-Jay", "Prinay", "Prince", "Prithvi", "Promise", "Puneetpaul", "Pushkar", "Qasim", "Qirui", "Quinlan", "Quinn", "Radmiras", "Raees", "Raegan", "Rafael", "Rafal", "Rafferty", "Rafi", "Raheem", "Rahil", "Rahim", "Rahman", "Raith", "Raithin", "Raja", "Rajab-Ali", "Rajan", "Ralfs", "Ralph", "Ramanas", "Ramit", "Ramone", "Ramsay", "Ramsey", "Rana", "Ranolph", "Raphael", "Rasmus", "Rasul", "Raul", "Raunaq", "Ravin", "Ray", "Rayaan", "Rayan", "Rayane", "Rayden", "Rayhan", "Raymond", "Rayne", "Rayyan", "Raza", "Reace", "Reagan", "Reean", "Reece", "Reed", "Reegan", "Rees", "Reese", "Reeve", "Regan", "Regean", "Reggie", "Rehaan", "Rehan", "Reice", "Reid", "Reigan", "Reilly", "Reily", "Reis", "Reiss", "Remigiusz", "Remo", "Remy", "Ren", "Renars", "Reng", "Rennie", "Reno", "Reo", "Reuben", "Rexford", "Reynold", "Rhein", "Rheo", "Rhett", "Rheyden", "Rhian", "Rhoan", "Rholmark", "Rhoridh", "Rhuairidh", "Rhuan", "Rhuaridh", "Rhudi", "Rhy", "Rhyan", "Rhyley", "Rhyon", "Rhys", "Rhys-Bernard", "Rhyse", "Riach", "Rian", "Ricards", "Riccardo", "Ricco", "Rice", "Richard", "Richey", "Richie", "Ricky", "Rico", "Ridley", "Ridwan", "Rihab", "Rihan", "Rihards", "Rihonn", "Rikki", "Riley", "Rio", "Rioden", "Rishi", "Ritchie", "Rivan", "Riyadh", "Riyaj", "Roan", "Roark", "Roary", "Rob", "Robbi", "Robbie", "Robbie-lee", "Robby", "Robert", "Robert-Gordon", "Robertjohn", "Robi", "Robin", "Rocco", "Roddy", "Roderick", "Rodrigo", "Roen", "Rogan", "Roger", "Rohaan", "Rohan", "Rohin", "Rohit", "Rokas", "Roman", "Ronald", "Ronan", "Ronan-Benedict", "Ronin", "Ronnie", "Rooke", "Roray", "Rori", "Rorie", "Rory", "Roshan", "Ross", "Ross-Andrew", "Rossi", "Rowan", "Rowen", "Roy", "Ruadhan", "Ruaidhri", "Ruairi", "Ruairidh", "Ruan", "Ruaraidh", "Ruari", "Ruaridh", "Ruben", "Rubhan", "Rubin", "Rubyn", "Rudi", "Rudy", "Rufus", "Rui", "Ruo", "Rupert", "Ruslan", "Russel", "Russell", "Ryaan", "Ryan", "Ryan-Lee", "Ryden", "Ryder", "Ryese", "Ryhs", "Rylan", "Rylay", "Rylee", "Ryleigh", "Ryley", "Rylie", "Ryo", "Ryszard", "Saad", "Sabeen", "Sachkirat", "Saffi", "Saghun", "Sahaib", "Sahbian", "Sahil", "Saif", "Saifaddine", "Saim", "Sajid", "Sajjad", "Salahudin", "Salman", "Salter", "Salvador", "Sam", "Saman", "Samar", "Samarjit", "Samatar", "Sambrid", "Sameer", "Sami", "Samir", "Sami-Ullah", "Samual", "Samuel", "Samuela", "Samy", "Sanaullah", "Sandro", "Sandy", "Sanfur", "Sanjay", "Santiago", "Santino", "Satveer", "Saul", "Saunders", "Savin", "Sayad", "Sayeed", "Sayf", "Scot", "Scott", "Scott-Alexander", "Seaan", "Seamas", "Seamus", "Sean", "Seane", "Sean-James", "Sean-Paul", "Sean-Ray", "Seb", "Sebastian", "Sebastien", "Selasi", "Seonaidh", "Sephiroth", "Sergei", "Sergio", "Seth", "Sethu", "Seumas", "Shaarvin", "Shadow", "Shae", "Shahmir", "Shai", "Shane", "Shannon", "Sharland", "Sharoz", "Shaughn", "Shaun", "Shaunpaul", "Shaun-Paul", "Shaun-Thomas", "Shaurya", "Shaw", "Shawn", "Shawnpaul", "Shay", "Shayaan", "Shayan", "Shaye", "Shayne", "Shazil", "Shea", "Sheafan", "Sheigh", "Shenuk", "Sher", "Shergo", "Sheriff", "Sherwyn", "Shiloh", "Shiraz", "Shreeram", "Shreyas", "Shyam", "Siddhant", "Siddharth", "Sidharth", "Sidney", "Siergiej", "Silas", "Simon", "Sinai", "Skye", "Sofian", "Sohaib", "Sohail", "Soham", "Sohan", "Sol", "Solomon", "Sonneey", "Sonni", "Sonny", "Sorley", "Soul", "Spencer", "Spondon", "Stanislaw", "Stanley", "Stefan", "Stefano", "Stefin", "Stephen", "Stephenjunior", "Steve", "Steven", "Steven-lee", "Stevie", "Stewart", "Stewarty", "Strachan", "Struan", "Stuart", "Su", "Subhaan", "Sudais", "Suheyb", "Suilven", "Sukhi", "Sukhpal", "Sukhvir", "Sulayman", "Sullivan", "Sultan", "Sung", "Sunny", "Suraj", "Surien", "Sweyn", "Syed", "Sylvain", "Symon", "Szymon", "Tadd", "Taddy", "Tadhg", "Taegan", "Taegen", "Tai", "Tait", "Taiwo", "Talha", "Taliesin", "Talon", "Talorcan", "Tamar", "Tamiem", "Tammam", "Tanay", "Tane", "Tanner", "Tanvir", "Tanzeel", "Taonga", "Tarik", "Tariq-Jay", "Tate", "Taylan", "Taylar", "Tayler", "Taylor", "Taylor-Jay", "Taylor-Lee", "Tayo", "Tayyab", "Tayye", "Tayyib", "Teagan", "Tee", "Teejay", "Tee-jay", "Tegan", "Teighen", "Teiyib", "Te-Jay", "Temba", "Teo", "Teodor", "Teos", "Terry", "Teydren", "Theo", "Theodore", "Thiago", "Thierry", "Thom", "Thomas", "Thomas-Jay", "Thomson", "Thorben", "Thorfinn", "Thrinei", "Thumbiko", "Tiago", "Tian", "Tiarnan", "Tibet", "Tieran", "Tiernan", "Timothy", "Timucin", "Tiree", "Tisloh", "Titi", "Titus", "Tiylar", "TJ", "Tjay", "T-Jay", "Tobey", "Tobi", "Tobias", "Tobie", "Toby", "Todd", "Tokinaga", "Toluwalase", "Tom", "Tomas", "Tomasz", "Tommi-Lee", "Tommy", "Tomson", "Tony", "Torin", "Torquil", "Torran", "Torrin", "Torsten", "Trafford", "Trai", "Travis", "Tre", "Trent", "Trey", "Tristain", "Tristan", "Troy", "Tubagus", "Turki", "Turner", "Ty", "Ty-Alexander", "Tye", "Tyelor", "Tylar", "Tyler", "Tyler-James", "Tyler-Jay", "Tyllor", "Tylor", "Tymom", "Tymon", "Tymoteusz", "Tyra", "Tyree", "Tyrnan", "Tyrone", "Tyson", "Ubaid", "Ubayd", "Uchenna", "Uilleam", "Umair", "Umar", "Umer", "Umut", "Urban", "Uri", "Usman", "Uzair", "Uzayr", "Valen", "Valentin", "Valentino", "Valery", "Valo", "Vasyl", "Vedantsinh", "Veeran", "Victor", "Victory", "Vinay", "Vince", "Vincent", "Vincenzo", "Vinh", "Vinnie", "Vithujan", "Vladimir", "Vladislav", "Vrishin", "Vuyolwethu", "Wabuya", "Wai", "Walid", "Wallace", "Walter", "Waqaas", "Warkhas", "Warren", "Warrick", "Wasif", "Wayde", "Wayne", "Wei", "Wen", "Wesley", "Wesley-Scott", "Wiktor", "Wilkie", "Will", "William", "William-John", "Willum", "Wilson", "Windsor", "Wojciech", "Woyenbrakemi", "Wyatt", "Wylie", "Wynn", "Xabier", "Xander", "Xavier", "Xiao", "Xida", "Xin", "Xue", "Yadgor", "Yago", "Yahya", "Yakup", "Yang", "Yanick", "Yann", "Yannick", "Yaseen", "Yasin", "Yasir", "Yassin", "Yoji", "Yong", "Yoolgeun", "Yorgos", "Youcef", "Yousif", "Youssef", "Yu", "Yuanyu", "Yuri", "Yusef", "Yusuf", "Yves", "Zaaine", "Zaak", "Zac", "Zach", "Zachariah", "Zacharias", "Zacharie", "Zacharius", "Zachariya", "Zachary", "Zachary-Marc", "Zachery", "Zack", "Zackary", "Zaid", "Zain", "Zaine", "Zaineddine", "Zainedin", "Zak", "Zakaria", "Zakariya", "Zakary", "Zaki", "Zakir", "Zakk", "Zamaar", "Zander", "Zane", "Zarran", "Zayd", "Zayn", "Zayne", "Ze", "Zechariah", "Zeek", "Zeeshan", "Zeid", "Zein", "Zen", "Zendel", "Zenith", "Zennon", "Zeph", "Zerah", "Zhen", "Zhi", "Zhong", "Zhuo", "Zi", "Zidane", "Zijie", "Zinedine", "Zion", "Zishan", "Ziya", "Ziyaan", "Zohaib", "Zohair", "Zoubaeir", "Zubair", "Zubayr", "Zuriel"]

# simple class for each team
class Team:

    # includes name and empty dictionary to store players
    def __init__(self, name):
        self.name = name
        self.players = gen_players(0)
        self.roster = []
        self.wins = 0
        self.losses = 0
        self.avgpts = 0.0   
        self.gamescores = []
        self.lineup = []


# class for a game
class Match:

    def __init__(self, t1, t2):
        t1.roster = rosterize(t1.players, "t1")
        t2.roster = rosterize(t2.players, "t2")
        t1.lineup = t1.roster[:5]
        t2.lineup = t2.roster[:5]

        self.teams = {"t1": t1,
                       "t2": t2}
        self.lineups = {"t1": t1.lineup,
                       "t2": t2.lineup}
        self.scores = {"t1": 0,
                       "t2": 0}
        
        self.haspossession = "t1" # tracks which team has possession (t1, t2)
        self.defending = "t2"
        self.pwithball = 0 # index of player with ball

        self.gametime = 0.00
        self.totalpossessions = 0
        self.quarter = 1
        self.quartertime = 720
        self.offthebats = 0
        self.shots = 0
        self.passes = 0
        self.violations = 0


    def play(self):

        # sim possessions til game ends

        while self.gametime < 2880:
            self.simPossession()

            if self.quartertime <= 0:
                self.quarter += 1
                self.quartertime = 720

        print(f"{self.teams["t1"].name} Score: {self.scores["t1"]}\n {self.teams["t2"].name} Score: {self.scores["t2"]}")
        print(f"{self.totalpossessions} Possessions")
        self.showStats()
        self.showMatchups()

    def showMatchups(self):

        for player in self.lineups["t1"] + self.lineups["t2"]:
            print(f"{player.data.get("Name")} defended by {player.matchup}")

    def simPossession(self):

        off_lineup = self.lineups[self.haspossession]
        def_lineup = self.lineups[self.defending]

        self.staminaCheck(off_lineup)

        self.decideMatchups(off_lineup, def_lineup)
        
        if self.quartertime < 24:
            shotclock = self.quartertime
        
        shotclock = 24
        time_elapsed = 0

        while shotclock > 0:
            # get team position, and choose team goal (what shot, how fast, iso or run play)
            teampos = self.getTeamPos()
            goal = self.chooseGoal(teampos=teampos)

            if goal == "giveUp":
                time_elapsed = 24
                break

            # choose player and matchup
            shooter = self.choosePlayer(goal, off_lineup)
            matchup = shooter.matchup

            # run attempt
            shot = self.shootIt(shooter, matchup, goal, shotclock)

            # if score, add to point totals and other stats
            time_elapsed = shot[1]
            shotclock -= time_elapsed

            if shotclock < 0:
                break

            shooter.subtractStamina(time_elapsed)

            if "made" in shot[0]:
                shooter.logShot(shot[0])

                # run assist check
                if goal["play"] == "play":
                    if self.assistCheck():
                        poss_assisters = set(off_lineup)
                        poss_assisters.remove(shooter)
                        assister = self.chooseAssister(list(poss_assisters))
                        assister.assists += 1

                match goal["shot"]:
                    
                    case "three":
                        self.scores[self.haspossession] += 3
                        break

                    case "mid":
                        self.scores[self.haspossession] += 2
                        break

                    case "lay":
                        self.scores[self.haspossession] += 3
                        break

            # if miss, decide who (which team/player) gets rebound
            elif "missed" in shot[0]:
                shooter.logShot(shot[0])

                rebound = self.checkRebound(off_lineup, def_lineup)
                match rebound:
                    case "offense":
                        # if offensive rebound, set clock to 14
                        shotclock = 14
                        self.totalpossessions += 1
                        self.gametime += time_elapsed
                        
                    case "defense":
                        # if defensive rebound
                        break

            elif "turnover" in shot[0]:
                # if turnover, switch which team has possesion and end the possession
                break
        
        self.quartertime -= time_elapsed
        self.gametime += time_elapsed
        self.switchPos()
        self.totalpossessions += 1

        return
    
    def staminaCheck(self, lineup):

        tapped_out = []
        for player in lineup:
            if player.stamina < 0:
                tapped_out.append(player)

        if len(tapped_out) > 0:
            subs = self.getSubs(len(tapped_out), self.teams[self.haspossession].roster, tapped_out, lineup)
            new_lineup = [player for player in lineup if player not in tapped_out] + subs
            self.lineups[self.haspossession] = new_lineup
    
    def getSubs(self, num, roster, tapped_out, current_lineup):
        '''chooses who to sub in next (highest avg offensive stats for now)'''
        available_options = {player for player in roster if player not in tapped_out + current_lineup}

        subs = []
        for i in range(num):
            candidate = list(available_options)[0]
            for player in available_options:
                candsum = sum([candidate.threeshot, candidate.midshot, candidate.layshot])
                playersum = sum([player.threeshot, player.midshot, player.layshot])
                if playersum > candsum:
                    candidate = player
            available_options.remove(candidate)
            subs.append(candidate)

        return subs


    def assistCheck(self):

        ast_odds = 0.35

        outcome = flip((ast_odds, True), (1.00 - ast_odds, False))

        return outcome
    
    def chooseAssister(self, lineup):

        n = 3

        assister_list = self.getBestAttribute("Pass", n, lineup)

        assister = flip((0.33, assister_list[n - n]),
                        (0.33, assister_list[n - (n - 1)]),
                        (0.34, assister_list[n - (n - 2)]))
        
        return assister
    
    def getMatchup(self, player, opp_lineup, strength):
        '''
        accepts a player and opposing lineup, and returns their best defensive matchup
        '''
        
        # get player strengths
        #strength = self.getOffTalents(player)

        opp_lineup = list(opp_lineup)

        # find defender that can best address those strengths
        match strength:
            case "ThreeShot" | "MidShot":
                golden_boy = self.getBestAttribute("PerDef", 1, opp_lineup)[0]
            case default:
                golden_boy = self.getBestAttribute("PaintDef", 1, opp_lineup)[0]

        return golden_boy

    def decideMatchups(self, off_lineup, def_lineup):
        
        '''
        decides the defensive matchup for each player on the floor
        '''

        off_shoot_rankings = sorted(off_lineup, key=lambda player: player.threeshot, reverse=True)
        def_set = set(def_lineup)

        for player in off_shoot_rankings:
            matchup = self.getMatchup(player, def_set, "ThreeShot")
            def_set.remove(matchup)
            player.matchup = matchup

    
    def getOffTalents(self, player):
        '''
        gets a player's best offensive attribute
        '''
        off_data = {k: v for k, v in player.data.items() if k == "ThreeShot" or k == "MidShot" or k == "LayShot"}
        reverse_data = {v: k for k, v in off_data.items()}

        best_att = reverse_data[max(reverse_data.keys())]

        return best_att

    def switchPos(self):
        '''
        switches which team has poessession
        '''

        temp = self.haspossession
        self.haspossession = self.defending
        self.defending = temp

        return
            

    def checkRebound(self, offense, defense):
        '''
        checks which team walks away with a rebound (coinflip for now)
        '''
        # TODO: make complex
        
        coin = flip((0.50, "offense"), (0.5, "defense"))
        return coin


    def choosePlayer(self, goal, lineup):
        '''
        picks which player will shoot, returns playerobj
        '''

        match goal["play"]:
            case "iso":
                match goal["shot"]:
                    case "three":
                        top_two = self.getBestIso(type="three", lineup=lineup)
                        shooter = flip((0.50, top_two[0]), (0.50, top_two[1]))
                    case "mid":
                        top_two = self.getBestIso(type="mid", lineup=lineup)
                        shooter = flip((0.50, top_two[0]), (0.50, top_two[1]))
                    case "lay":
                        top_two = self.getBestIso(type="lay", lineup=lineup)
                        shooter = flip((0.50, top_two[0]), (0.50, top_two[1]))
            case "play":
                match goal["shot"]:
                    case "three":
                        top_three = self.getBestShooters("three", lineup, 3)
                        shooter = flip((0.33, top_three[0]), (0.33, top_three[1]), (0.34, top_three[2]))
                    case "mid":
                        top_three = self.getBestShooters("mid", lineup, 3)
                        shooter = flip((0.33, top_three[0]), (0.33, top_three[1]), (0.34, top_three[2]))
                    case "lay":
                        top_three = self.getBestShooters("lay", lineup, 3)
                        shooter = flip((0.33, top_three[0]), (0.33, top_three[1]), (0.34, top_three[2]))
        
        return shooter

    def getBestShooters(self, type, lineup, num):
        '''
        returns the best players in a lineup with a given shot attribute and number to return 
        '''
        onfloor = lineup.copy()

        best_shooters = []
        for x in range(num):
            best_shooter = onfloor[0]
            for i in range(len(onfloor)):
                match type:
                    case "three":
                        if onfloor[i].threeshot > best_shooter.threeshot:
                            best_shooter = onfloor[i]
                            index = i
                        elif onfloor[i].threeshot == best_shooter.threeshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_shooter = onfloor[i]
                                    index = i
                                case 0:
                                    index = i
                    case "mid":
                        if onfloor[i].midshot > best_shooter.midshot:
                            best_shooter = onfloor[i]
                            index = i
                        elif onfloor[i].midshot == best_shooter.midshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_shooter = onfloor[i]
                                    index = i
                                case 0:
                                    index = i
                    case "lay":
                        if onfloor[i].layshot > best_shooter.layshot:
                            best_shooter = onfloor[i]
                            index = i
                        elif onfloor[i].layshot == best_shooter.layshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_shooter = onfloor[i]
                                    index = i
                                case 0:
                                    index = i
            best_shooters.append(best_shooter)
            onfloor.pop(index)

        return best_shooters



    def getBestIso(self, type, lineup):
        '''
        returns the best iso scorer on the floor at the moment
        '''
        on_floor = lineup.copy()

        best_handlers = []
        for x in range(3):
            best_handler = on_floor[0]
            for i in range(len(on_floor)):
                if on_floor[i].ballhandle > best_handler.ballhandle:
                    best_handler = on_floor[i]
                    index = i
                elif on_floor[i].ballhandle == best_handler.ballhandle:
                    coin = rand.randint(0, 1)
                    match coin:
                        case 1:
                            best_handler = on_floor[i]
                            index = i
                        case 0:
                            index = i
            best_handlers.append(best_handler)
            on_floor.pop(index) # fix again
 
        
        best_isos = self.getBestShooters(type=type, lineup=best_handlers, num=2)
        
        return best_isos
        
    def getBestAttribute(self, attr, num, lineup):
        '''
        takes a given attribute, lineup, and number, and returns the given number of players with the best of the given attribute
        '''
        attr = attr.lower()

        onfloor = lineup.copy()
        best_players = []

        for x in range(num):
            best_player = onfloor[0]
            for i in range(len(onfloor)):
                index = i
                match attr:
                    case "three":
                        if onfloor[i].threeshot > best_player.threeshot:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].threeshot == best_player.threeshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                   # index = i
                                case 0:
                                    pass
                    case "mid":
                        if onfloor[i].midshot > best_player.midshot:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].midshot == best_player.midshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                   # index = i
                                case 0:
                                  #  index = i
                                  pass
                    case "lay":
                        if onfloor[i].layshot > best_player.layshot:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].layshot == best_player.layshot:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                   # index = i
                                case 0:
                                   # index = i
                                    pass
                    case "perdef":
                        if onfloor[i].perdef > best_player.perdef:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].perdef == best_player.perdef:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                  #  index = i
                                case 0:
                                    #index = i
                                    pass
                    case "paintdef":
                        if onfloor[i].paintdef > best_player.paintdef:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].paintdef == best_player.paintdef:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                   # index = i
                                case 0:
                                   # index = i    
                                   pass
                    case "pass":
                        if onfloor[i].passodds > best_player.passodds:
                            best_player = onfloor[i]
                            index = i
                        elif onfloor[i].passodds == best_player.passodds:
                            coin = rand.randint(0, 1)
                            match coin:
                                case 1:
                                    best_player = onfloor[i]
                                case 0:
                                   pass
                    case default:
                        raise ValueError(f"No attribute provided, recevied {default} instead")
                    
            best_players.append(best_player)
            onfloor.pop(index)

        return best_players
            
    def chooseGoal(self, teampos):
        '''
        takes in team position and returns a dictionary with "shot" shottype, "play" playtype, and "pace" pace
        '''

        match teampos:

            case "scoreFast":
                three_odds = 0.55
                mid_odds = 0.22
                lay_odds = 0.23
                play_odds = 0.40
                iso_odds = 0.60
            case "needThree":
                three_odds = 1.0
                mid_odds = 0.0
                lay_odds = 0.0
                play_odds = 0.20
                iso_odds = 0.80
            case "scoreNormal":
                three_odds = 0.42
                mid_odds = 0.29
                lay_odds = 0.29
                play_odds = 0.60
                iso_odds = 0.40
            case "scoreSlow":
                three_odds = 0.33
                mid_odds = 0.34
                lay_odds = 0.33
                play_odds = 0.80
                iso_odds = 0.20
            case "giveUp":
                return "giveUp"
            
        stype = flip((three_odds, "three"), (mid_odds, "mid"), (lay_odds, "lay"))
        ptype = flip((play_odds, "play"), (iso_odds, "iso"))
        
        return {"shot": stype, "play": ptype, "pace": teampos}
    
    def getTeamPos(self):
        '''
        gets the team position based on point differential and overall game time
        feeds into second function to account for shotclock
        '''
        score = self.scores[self.haspossession]
        oppscore = self.scores[self.defending]
        diff = score - oppscore
        
        if diff <= -15:
            if self.gametime < 2820:
                pace = "scoreFast"
            else:
                pace = "giveUp"
        elif diff <= -3:
            if self.gametime > 2790:
                pace = "needThree"
            else:
                pace = "scoreNormal"
        elif diff < 0:
            if self.gametime < 2790:
                pace = "scoreNormal"
            else:
                pace = "scoreFast"
        elif diff == 0:
            pace = "scoreNormal"
        elif diff > 0 and diff < 10:
            pace = "scoreSlow"
        else:
            if self.gametime >= 2820:
                pace = "giveUp"
            else:
                pace = "scoreSlow"
            
        return pace


    def shootIt(self, player, matchup, goal, shotclock):
        '''
        takes player, matchup, and goal -> returns (outcome of shot, time elapsed)
        '''

        # calculate time spent depending on if it's a play or an iso possession, the player's ballhandle, and the time left
        time_elapsed = self.getTimeSpent(goal, shotclock)
        
        # take the shot 
        shot = self.getShotOutcome(player, matchup, goal)

        # return time spent and outcome
        return (shot, time_elapsed)

    
    def getShotOutcome(self, player, matchup, goal):
        '''
        gets the outcome of a play based on player attributes, will eventually have chance for turnover
        '''
        threescale = 100 * 1.2375 # 99 = 80% when open
        midscale = 100 * 1.32 # 99 = 85% when open 
        layscale = 100 * 1.042 # 99 = 90% when open
        perdefscale = 100 * 2.625 # 99 = 42.3% guarded fg
        middefscale = 100 * 2.166 # 99 = 45.7% guarded fg
        paintdefscale = 100 * 1.6445 # 99 = 60.2% guarded fg

        if self.checkTurnover(matchup):
            return "turnover"

        match goal["shot"]:

            case "three":
                threeweight = round(player.threeshot / threescale, 2)
                defweight = round(matchup.perdef / perdefscale, 2)
                threeweight -= defweight
                missweight = 1.0 - threeweight

                outcome = flip((threeweight, "threemade"), (missweight, "threemissed"))

            case "mid":
                midweight = round(player.midshot / midscale, 2)
                defweight = round(matchup.perdef / middefscale, 2)
                midweight -= defweight
                missweight = 1.0 - midweight
                
                outcome = flip((midweight, "midmade"), (missweight, "midmissed"))

            case "lay":
                layweight = round(player.layshot / layscale, 2)
                defweight = round(matchup.paintdef / paintdefscale, 2)
                layweight -= defweight
                missweight = 1.0 - layweight
                
                outcome = flip((layweight, "laymade"), (missweight, "laymissed"))

        return outcome

    def checkTurnover(self, matchup):
        '''
        barebones function to check for turnovers, depends on defender steal
        '''
        defweight = round(matchup.stl / 500, 2)
        ovrweight = 1 - defweight

        turnover = flip((defweight, "steal"), (ovrweight, "nosteal"))

        if turnover[1] == "steal":
            return True
        
        return False


    def getTimeSpent(self, goal, shotclock):
        '''
        takes in goal and returns time elapsed during play (up until shot taken) - depends on play and pace
        '''

        # catch final second shots up here:
        if shotclock <= 3:
            return shotclock


        match goal["play"]:

            case "iso":

                match goal["pace"]:

                    case "scoreNormal":

                        timeSpent = rand.triangular(6, shotclock, ((1/2) * shotclock))
                        return timeSpent
                    
                    case "scoreFast":

                        timeSpent = rand.triangular(4, shotclock, ((1.5/4) * shotclock))
                        return timeSpent
                    
                    case "scoreSlow":

                        timeSpent = rand.triangular(7, shotclock, ((3/4) * shotclock))
                        return timeSpent
                    
                    case "needThree":
                        timeSpent = rand.triangular(0, shotclock, ((1/4) * shotclock))
                        return timeSpent

            case "play":
                
                match goal["pace"]:

                    case "scoreNormal":

                        timeSpent = rand.triangular(6.5, shotclock, ((2/3) * shotclock))
                        return timeSpent
                    
                    case "scoreFast":

                        timeSpent = rand.triangular(5, shotclock, ((1.2/3) * shotclock))
                        return timeSpent
                    
                    case "scoreSlow":

                        timeSpent = rand.triangular(7.5, shotclock, ((3/4) * shotclock))
                        return timeSpent
                    
                    case "needThree":
                        timeSpent = rand.triangular(0, shotclock, ((1.2/4) * shotclock))
                        return timeSpent

    def showStats(self):

            for player in self.lineups["t1"]:
                print(f"{player.data.get('Name')}: {player.points} points, {player.threes} threes")
            for player in self.lineups["t2"]:
                print(f"{player.data.get('Name')}: {player.points} points, {player.threes} threes")
        



        


class Player:

    def __init__(self, data, i, team):
        self.team = team
        self.data = data
        self.index = i
        
        self.shotodds = data.get("ShotTend")
        self.threeodds = data.get("ThreeTend")
        self.midodds = data.get("MidTend")
        self.layodds = data.get("LayTend")
        self.passodds = data.get("Pass")
        self.threeshot = data.get("ThreeShot")
        self.midshot = data.get("MidShot")
        self.layshot = data.get("LayShot")
        self.stl = data.get("Stl")
        self.perdef = data.get("PerDef")
        self.paintdef = data.get("PaintDef")
        self.ballhandle = data.get("BallHandle") # need to add still
        
        
        self.matchup = None
        self.stamina = 100
        self.points = 0
        self.threes = 0
        self.mids = 0
        self.lays = 0
        self.assists = 0
        self.shottot = 0
        self.shotsmade = 0
    
    @property
    def game_stats(self):
        stat_dict = {
            "name": self.data.get("Name")[0] + ". " + self.data.get("Name").split(" ")[-1],
            "pts": self.points,
            "ast": self.assists,
            "threes": self.threes,
            "fg%": self.fgper
        }

        return stat_dict

    @property
    def fgper(self):
        
        if self.shottot > 0:
            fgper = round((self.shotsmade / self.shottot) * 100, 1)
        else:
            fgper = 0
        return fgper
    
    def __hash__(self) -> int:

        val = sum([self.ballhandle, self.layodds, self.shotodds, self.midshot, self.layshot, self.threeshot, self.data.get("PlayerID")])
        return val
    
    def __eq__(self, other: object) -> bool:
        
        if not isinstance(other, Player):
            raise ValueError

        if other.data == self.data:
            return True
        return False

    def subtractStamina(self, shottime):

        time_ratio = shottime / 24

        self.stamina -= time_ratio * 10

    def logShot(self, outcome):
        '''
        logs shot in player stats   
        '''

        match outcome:

            case "threemade":
                self.threes += 1
                self.shottot += 1
                self.points += 3
                self.shotsmade += 1

            case "threemissed":
                self.shottot += 1
            
            case "midmade":
                self.mids += 1
                self.shottot += 1
                self.points += 2
                self.shotsmade += 1

            case "midmissed":
                self.shottot += 1
                
            case "laymade":
                self.lays += 1
                self.shottot += 1
                self.shotsmade += 1
                self.points += 2

            case "laymissed":
                self.shottot += 1
        return
    
    def __str__(self):

        return self.data.get("Name")

def flip(*args):
        '''
        Each argument is a tuple formatted as such:
        [0] - corresponds to probability of event
        [1] - corresponds to the event itself
        '''
        # create list to store dictionaries that contain the range for each event and the event name
        ranges = []
        start = 0

        # iterate through arguments and get the decimal range for each outcome
        for tup in args:
            stop = start + tup[0]
            event = tup[1]
            ranges.append({
                "start": start,
                "stop": stop,
                "event": event
            })
            start = stop

        # get random number
        sample = rand.uniform(0.01, 1.0)

        # check where number falls in ranges
        for rang in ranges:
            if sample > rang["start"] and sample <= rang["stop"]:
                outcome = rang["event"]

        return outcome


# takes in a dictionary of players, and spits out a list of player objects containing the player data - used in match simulation
def rosterize(playersdict, team): 

    # for now, this function has hard coded modes just to divide up starting and bench lineup
    playerlist = []

    
    for i in range(len(playersdict["PlayerID"])):
        playerdata = {key: value[i] for (key, value) in zip(playersdict.keys(), playersdict.values())}
        playerobj = Player(playerdata, i, team)
        playerlist.append(playerobj)
    
    # elif mode == "bench":
    #     for i in range(5, 10):
    #         playerdata = {key: value[i] for (key, value) in zip(playersdict.keys(), playersdict.values())}
    #         playerobj = Player(playerdata, (i - 5), team)
    #         playerlist.append(playerobj)

    return playerlist


# generate a given amount of players (random)
def gen_players(amount):
    
    dict = {"PlayerID": [], "Name": [], "ThreeShot": [], "MidShot": [], "LayShot": [], "PerDef": [], "PaintDef": [], "Stl": [], "ShotTend": [], "ThreeTend": []
            , "MidTend": [], "LayTend": [], "Pass": []}
    for i in range(amount):
        dict["PlayerID"].append(i)
        dict["Name"].append(names[rand.randint(0, len(names) - 1)])
        dict["ThreeShot"].append(rand.randint(40, 100))
        dict["MidShot"].append(rand.randint(40, 100))
        dict["LayShot"].append(rand.randint(40, 100))
        dict["PerDef"].append(rand.randint(40, 100))
        dict["PaintDef"].append(rand.randint(40, 100))
        dict["Stl"].append(rand.randint(20, 70))

        dict["ShotTend"].append(rand.randint(20, 70))
        dict["ThreeTend"].append(rand.randint(20, 70))
        dict["MidTend"].append(rand.randint(20, 70))
        dict["LayTend"].append(rand.randint(20, 70))
        dict["Pass"].append(rand.randint(20, 70))
        
        
    
    return dict




# takes in two team objects, generates players, and assigns them to each team
def initializeTeams(t1, t2):

    players = gen_players(10) # get players

    attributes = ["PlayerID", "Name", "ThreeShot", "MidShot", "LayShot", "PerDef", "PaintDef", "Stl", "ShotTend", "ThreeTend", "MidTend", "LayTend", "Pass"]

    # team 1 loop
    for i in range(5):
        # select a random player
        playertoadd = rand.randint(0, len(players["PlayerID"]) - 1)

        # add to team 1
        for attribute in attributes:
            t1.players[attribute].append(players[attribute][playertoadd])
            players[attribute].pop(playertoadd) # remove from player list

    # team 2 loop
    for i in range(5):

        playertoadd = rand.randint(0, len(players["PlayerID"]) - 1)

        for attribute in attributes:
            t2.players[attribute].append(players[attribute][playertoadd])
            players[attribute].pop(playertoadd)

    return

# writes teams to json file
def save_teams(teams):
    '''
    pass list of team objects as arguments
    store teams into dictionary
    write dict as json string

    '''
    teamdict = {}

    for team in teams:
        # add team as entry in dict
        teamdict[team.name] = team.__dict__

    with open("newteams.json", "w") as file:
        file.write(json.dumps(teamdict, indent=6))
    


# reads json file of teams
def load_teams(file_path):
    '''
    create dictionary of teams to return
    open file
    write json to dictionary

    '''

    teams = {}
    with open(file_path, "r") as file:
        teams = json.load(file)

    return teams

# converts a dictionary containing a team to a team object
def dict_to_team(dct):
    teamobj = Team(dct["name"])
    teamobj.players = dct["players"]
    teamobj.wins = dct["wins"]
    teamobj.losses = dct["losses"]
    
    return teamobj

# controls everything
# def main():

#     teamdict = load_teams("testteams.json")
#     mice = dict_to_team(teamdict["Knicks"])
#     snakes = dict_to_team(teamdict["Cavs"])

#     while True:
#         sim = input("press enter to sim a match")
#         if sim == "":
#             game = Match(mice, snakes)
#             game.play()
#         else:
#             break

#     #save_teams([mice, snakes])

# main()
