'''
ROUGH WIP PLAY-BY-PLAY SIM
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
        self.wins = 0
        self.losses = 0
        self.avgpts = 0.0
        self.gamescores = []

# class for a game
class Match:

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        self.t1rost = rosterize(t1.players, "t1")
        self.t2rost = rosterize(t2.players, "t2")
        self.t1bench = rosterize(t1.players, "t1", "bench")
        self.t2bench = rosterize(t2.players, "t2", "bench")
        self.t1score = 0
        self.t2score = 0
        
        self.haspossession = self.t1rost # tracks which team has possession (t1, t2)
        self.pwithball = 0 # index of player with ball

        self.gametime = 0.00
        self.totalpossessions = 0
        self.quarter = 1
        self.possessionlens = []
        self.offthebats = 0
        self.shots = 0

      
        
    # controls the whole game
    def play(self):

        while self.gametime <= 2880:

            if self.quarter == 2:
                self.simPossession(self.t1bench, self.t2bench)
            else:
                self.simPossession(self.t1rost, self.t2rost)
            

        if self.t1score > self.t2score:
            self.t1.wins += 1
            self.t2.losses += 1
            print(f"The {self.t1.name} Win")    
        elif self.t2score > self.t1score:
            self.t2.wins += 1
            self.t1.losses += 1
            print(f"The {self.t2.name} Win")    
        
        print(f"Final Score: \nThe {self.t1.name}: {self.t1score} \nThe {self.t2.name}: {self.t2score}")
        t1best = self.getBestPlayer(self.t1rost)
        t2best = self.getBestPlayer(self.t2rost)

        print(f"The {self.t1.name} best player: {t1best.data.get('Name')}, with {t1best.points} points on {t1best.fgper}% shooting ({t1best.shotsmade}/{t1best.shottot}) with {t1best.threes} threes, {t1best.mids} midrange shots, and {t1best.lays} layups")
        print(f"The {self.t2.name} best player: {t2best.data.get('Name')}, with {t2best.points} points on {t2best.fgper}% shooting ({t2best.shotsmade}/{t2best.shottot}) with {t2best.threes} threes, {t2best.mids} midrange shots, and {t2best.lays} layups")
        print(self.totalpossessions)

        self.t1.gamescores.append(self.t1score)
        self.t2.gamescores.append(self.t2score)

        self.showStats()

        totallen = 0
        for x in self.possessionlens:
            totallen += x

        avglen = totallen / len(self.possessionlens)
        print(avglen)
        print(f"{self.offthebats} / {self.shots} shots were off rip")
        
    
    # quicklt shows the statline for every player on the starting rosters
    def showStats(self):

        for player in self.t1rost:
            print(f"{player.data.get('Name')}: {player.points} points, {player.fgper} fg%, {player.threes} threes")
        for player in self.t2rost:
            print(f"{player.data.get('Name')}: {player.points} points, {player.fgper} fg%, {player.threes} threes")
    
    def getBestPlayer(self, roster):

        bestboy = Player(data={}, team="poo", i=0)
        for player in roster:
            if player.points > bestboy.points:
                bestboy = player

        return bestboy



    # sims a possession given both lineups on the floor
    def simPossession(self, t1Lineup, t2Lineup):
        
        for x in t1Lineup:
            x.loc = "outside"
        for x in t2Lineup:
            x.loc = "outside"

        # shotclock
        shotclock = 24

        # ballhandler is set to specific player on specific team
        ballhandler = self.haspossession[self.pwithball]
        
        # get matchup
        # for now, a player's matchup is just the player their index corresponds to on the other team
        if ballhandler.team == "t1":
            matchup = t2Lineup[ballhandler.index]
            oppteam = t2Lineup
        else:
            matchup = t1Lineup[ballhandler.index]
            oppteam = t1Lineup

        while shotclock > 0:
            # stores amount to adjust score after possession
            amt = 0
            
            outcome = self.simPlay(ballhandler, matchup, shotclock)

            # check if time runs out during play
            if shotclock - outcome[1] > 0:
            
                # if turnover
                if outcome[0] == "turnov":
                    self.pwithball = matchup.index
                    shotclock -= outcome[1]
                    print("turnover")
                    break

                # if 3pointer
                elif outcome[0] == "threemade":
                    ballhandler.shotsmade += 1
                    ballhandler.shottot += 1
                    ballhandler.points += 3
                    ballhandler.logShot("three")
                    ballhandler.getFGPer()
                    amt = 3
                    shotclock -= outcome[1]
                    break
                elif outcome[0] == "threemissed":
                    ballhandler.shottot += 1
                    ballhandler.getFGPer()
                    shotclock -= outcome[1]
                    coinflip = rand.randint(0, 1)
                    if coinflip == 0:
                        pass
                    else:
                        self.pwithball = rand.choice(oppteam).index
                        break
                    
                # if middy
                elif outcome[0] == "midmade":
                    ballhandler.shotsmade += 1
                    ballhandler.shottot += 1
                    ballhandler.points += 2
                    ballhandler.logShot("mid")
                    ballhandler.getFGPer()
                    amt = 2
                    shotclock -= outcome[1]
                    break
                elif outcome[0] == "midmissed":
                    ballhandler.shottot += 1
                    ballhandler.getFGPer()
                    shotclock -= outcome[1]
                    coinflip = rand.randint(0, 1)
                    if coinflip == 0:
                        pass
                    else:
                        self.pwithball = rand.choice(oppteam).index
                        break

                # if layup
                elif outcome[0] == "laymade":
                    ballhandler.shotsmade += 1
                    ballhandler.shottot += 1
                    ballhandler.points += 2
                    ballhandler.logShot("lay")
                    ballhandler.getFGPer()
                    amt = 2
                    shotclock -= outcome[1]
                    break
                elif outcome[0] == "laymissed":
                    
                    ballhandler.shottot += 1
                    ballhandler.getFGPer()

                    shotclock -= outcome[1]
                    coinflip = rand.randint(0, 1)
                    if coinflip == 0:
                        pass
                    else:
                        self.pwithball = rand.choice(oppteam).index
                        break

                # if pass (currently passes to random player aside from the current ballhandler)
                elif outcome[0] == "passmade":
                    newhandler = rand.randint(0, 4)
                    while newhandler == ballhandler.index:
                        newhandler = rand.randint(0, 4)
                    ballhandler = self.haspossession[newhandler]
            else:
                break
                

        # update score
        self.updateScore(amt)

        # flip possession
        if matchup.team == "t1":
            self.haspossession = t1Lineup
        elif matchup.team == "t2":
            self.haspossession = t2Lineup

        if shotclock > 0:
            self.gametime += (24 - shotclock)
            self.possessionlens.append((24 - shotclock))
            print(24 - shotclock)
        else:
            self.gametime += 24
            self.possessionlens.append(24)
            print(24)


        self.totalpossessions += 1
        self.updateQuarter()

        return
    
    def updateQuarter(self):

        if self.gametime <= 720:
            self.quarter = 1
        elif self.gametime <= 1440 and self.gametime > 720:
            self.quarter = 2
        elif self.gametime <= 2160 and self.gametime > 1440:
            self.quarter = 3
        elif self.gametime <= 2880 and self.gametime > 2160:
            self.quarter = 4
    
    # returns outcome of play, and time ellapsed during play
    # TODO: put this logic in another method
    def simPlay(self, player, matchup, shotclock):

        timeElapsed = 0.0

        # scalars for each stat - hand tuned and based on real(ish) fg%
        threescale = 100 * 1.2375 # 99 = 80% when open
        midscale = 100 * 1.32 # 99 = 85% when open 
        layscale = 100 * 1.042 # 99 = 90% when open
        perdefscale = 100 * 2.625 # 99 = 42.3% guarded fg
        middefscale = 100 * 2.166 # 99 = 45.7% guarded fg
        paintdefscale = 100 * 1.6445 # 99 = 60.2% guarded fg

        # get current team position
        teampos = self.getTeamPos(player.team)
        
        # first, decide what the player will attempt - returns (destination, action)
        dec = player.newdecide(teampos, shotclock)

        # handle movement and itme spent moving (no defensive check for now)
        traveltime = self.getTravelTime(player, player.loc, dec[0])
        timeElapsed += traveltime
        player.loc = dec[0]

        # handle action
        if dec[1] == "shot":

            self.shots += 1
            if timeElapsed < 1.0:
                self.offthebats += 1
            
            if player.loc == "outside":
                threeweight = round(player.threeshot / threescale, 2)
                defweight = round(matchup.perdef / perdefscale, 2)
                threeweight -= defweight
                missweight = 1.0 - threeweight
                
                
                outcome = player.newflip((threeweight, "threemade"), (missweight, "threemissed"))
                timeElapsed += self.getShotTIme(player, shot="three", outcome=outcome)

            elif player.loc == "inside":
                midweight = round(player.midshot / midscale, 2)
                defweight = round(matchup.perdef / middefscale, 2)
                midweight -= defweight
                missweight = 1.0 - midweight

                outcome = player.newflip((midweight, "midmade"), (missweight, "midmissed"))
                timeElapsed += self.getShotTIme(player, shot="mid", outcome=outcome)
                

            elif player.loc == "close":
                layweight = round(player.layshot / layscale, 2)
                defweight = round(matchup.paintdef / paintdefscale, 2)
                layweight -= defweight
                missweight = 1.0 - layweight
                
                outcome = player.newflip((layweight, "laymade"), (missweight, "laymissed"))
                timeElapsed += self.getShotTIme(player, shot="lay", outcome=outcome)

                

        elif dec[1] == "pass":
            defweight = round(matchup.stl / 500, 2)
            ovrweight = 1 - defweight

            outcome = player.newflip((ovrweight, "passmade"), (defweight, "turnov"))

            timeElapsed += 1


        return (outcome, timeElapsed)
        
        '''
        # then run the attempt against their defender
        if dec == "three":
            threeweight = round(player.threeshot / threescale, 2)
            defweight = round(matchup.perdef / perdefscale, 2)
            ovrweight = threeweight - defweight

            outcome = player.flip(ovrweight)
            if outcome == "H":
                return ("threemade", 14)
            else:
                return ("threemissed", 16)
        
        # mid attempt
        elif dec == "mid":
            midweight = round(player.midshot / midscale, 2)
            defweight = round(matchup.perdef / middefscale, 2)
            ovrweight = midweight - defweight

            outcome = player.flip(ovrweight)
            if outcome == "H":
                return ("midmade", 14)
            else:
                return ("midmissed", 6)
        
        # lay attempt
        elif dec == "lay":
            layweight = round(player.layshot / layscale, 2)
            defweight = round(matchup.paintdef / paintdefscale, 2)
            ovrweight = layweight - defweight

            outcome = player.flip(ovrweight)
            if outcome == "H":
                return ("laymade", 14)
            else:
                return ("laymissed", 16)
        
        # pass attempt
        elif dec == "pass":
            defweight = round(matchup.stl / 500, 2)
            ovrweight = 1 - defweight

            outcome = player.flip(ovrweight)
            if outcome == "H":
                return ("passmade", 2)
            else:
                return ("turnov", 2)
        '''
    
    # calculates a player's time spent moving given the player, the starting location, and the destination
    def getTravelTime(self, player, start, dest):

        markers = {
            "outside":40,
            "inside": 20,
            "close": 0
        }

        speed = player.speed
        distance = abs(markers[start] - markers[dest])
        time = distance / speed
        
        #print(time)

        return time

    # returns time spent shooting given player, outcome and shot type
    def getShotTIme(self, player, shot, outcome):

        shotscale = 99 / 0.4

        if shot == "three":
            releaseTime = player.threeshot / shotscale
            reboundTime = 0
            if outcome == "threemissed":
                reboundTime += 3

        elif shot == "mid":
            releaseTime = player.midshot / shotscale
            reboundTime = 0
            if outcome == "midmissed":
                reboundTime += 2.5

        elif shot == "lay":
            releaseTime = player.layshot / shotscale
            reboundTime = 0
            if outcome == "laymissed":
                reboundTime += 1

    

        return releaseTime + reboundTime

    # calculates point differential
    def getTeamPos(self, team):

        if team == "t1":
            teampos = self.t1score - self.t2score
        else:
            teampos = self.t2score - self.t1score

        return teampos
            
    def updateScore(self, amount):

        if self.haspossession == self.t1rost:
            self.t1score += amount
        elif self.haspossession == self.t2rost:
            self.t2score += amount
            
        



        


class Player:

    def __init__(self, data, i, team):
        self.team = team
        self.data = data
        self.index = i
        
        self.shotodds = data.get("ShotTend")
        self.threeodds = data.get("ThreeTend")
        self.midodds = data.get("MidTend")
        self.layodds = data.get("LayTend")
        self.passodds = data.get("PassTend")
        self.threeshot = data.get("ThreeShot")
        self.midshot = data.get("MidShot")
        self.layshot = data.get("LayShot")
        self.stl = data.get("Stl")
        self.perdef = data.get("PerDef")
        self.paintdef = data.get("PaintDef")
        self.speed = data.get("Speed") # need to add still
        #self.handle = data.get("BallHandle") # need to add still
        #self.bestshot = self.getBestShot()
        
        self.loc = "outside"
        self.points = 0
        self.threes = 0
        self.mids = 0
        self.lays = 0
        self.shottot = 0
        self.shotsmade = 0
        self.fgper = 0

    # returns what the player will try to do, returns three, mid, lay, or pass
    def decide(self):

        # pass or shot
        shotweight = round(self.shotodds / 100, 2)
        por = self.flip(shotweight)

        if por == "H":
            # if shot, decide what kind, first roll for three, then roll for mid or layup if necessary
            threeweight = round(self.threeodds / 100, 2)
            shottype = self.flip(threeweight)

            if shottype == "H":
                decision = "three"
            else:
                midweight = round(self.midodds / 100, 2)
                layweight = round(self.layodds / 100, 2)
                endpoint = midweight + layweight

                shottype = self.flip(midweight, endpoint)

                if shottype == "H":
                    decision = "mid"
                else:
                    decision = "lay"
        else:
            decision = "pass"

        return decision

    
    # an updated verison of decide that updates player location to determine what shot they take, returns a tuple formatted as such: (destination, action)
    def newdecide(self, teampos, sclock):

        # compute odds for each possible decision
        shotweight = round(self.shotodds / 100, 2)
        passweight = round(self.passodds / 100, 2)

        threeweight = round(self.threeodds / 100, 2)
        midweight = round(self.midodds / 100, 2)
        layweight = round(self.layodds / 100, 2)


        # change offensive tempo depending on team's position in game, might change to string later
        if teampos <= -20:
            clocklimit = 10
        elif teampos <= -10 and teampos > -20:
            clocklimit = 8
        elif teampos > -10 and teampos < 0:
            clocklimit = 5
        elif teampos == 0:
            clocklimit = 3
        elif teampos > 0 and teampos < 10:
            clocklimit = 2
        elif teampos >= 10:
            clocklimit = 1

        
        # use shotclock to adjust pace (more likely to shoot as clocklimit is reached and surpassed)
        if sclock <= clocklimit:

            shotincrease = round((clocklimit / sclock) / 100, 2)

            shotweight += shotincrease
            passweight -= shotincrease
        
        
        # catch any negative values
        for val in [shotweight, passweight]:
            if val < 0:
                val = 0.0
        
        # first, run a movement/drive check
        drive = self.newflip((threeweight, "outside"), (midweight, "inside"), (layweight, "close"))

        # then, decide what the player will do at their location
        decision = self.newflip((shotweight, "shot"), (passweight, "pass"))

        return (drive, decision)


        

    # flips a biased coin to decide something, returns heads or tails, odds decided by probability and endpoint
    def flip(self, p, endp=1.0):

        sample = rand.uniform(0, endp)

        if sample < p:
            return "H"
        else:
            return "T"
    
    # takes tuples of events and probabilities, and returns which event will occur
    def newflip(self, *args):
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
        sample = rand.uniform(0, 1.0)

        # check where number falls in ranges
        for rang in ranges:
            if sample > rang["start"] and sample <= rang["stop"]:
                outcome = rang["event"]

        return outcome
    
    # gets the player's best shot for use in movement logic
    def getBestShot(self):

        shots = [self.threeshot, self.midshot, self.layshot]
        shotids = {
            0: "three",
            1: "mid",
            2: "lay,"
        }

        shotval = 0
        bestshot = ""
        for i in range(len(shots)):
            if shots[i] > bestshot:
                shotval = shots[i]
                bestshot = shotids[i]
            
        return bestshot    



    def getFGPer(self):
        if self.shottot <= 0:
            pass
        else:
            self.fgper = round((self.shotsmade / self.shottot) * 100)

    # logs the shot in players stats given the type
    def logShot(self, shottype):

        if shottype == "lay":
            self.lays += 1
        elif shottype == "three":
            self.threes += 1
        elif shottype == "mid":
            self.mids += 1

    


# takes in a dictionary of players, and spits out a list of player objects containing the player data - used in match simulation
def rosterize(playersdict, team, mode='start'): 

    # for now, this function has hard coded modes just to divide up starting and bench lineup
    playerlist = []

    if mode == 'start':
        for i in range(5):
            playerdata = {key: value[i] for (key, value) in zip(playersdict.keys(), playersdict.values())}
            playerobj = Player(playerdata, i, team)
            playerlist.append(playerobj)
    elif mode == "bench":
        for i in range(5, 10):
            playerdata = {key: value[i] for (key, value) in zip(playersdict.keys(), playersdict.values())}
            playerobj = Player(playerdata, (i - 5), team)
            playerlist.append(playerobj)

    return playerlist

def updateAveragePts(team):

    totalpts = 0
    for x in team.gamescores:
        totalpts += x

    team.avgpts = round(totalpts / len(team.gamescores), 1)
    

# generate a given amount of players (random)
def gen_players(amount):
    
    dict = {"PlayerID": [], "Name": [], "ThreeShot": [], "MidShot": [], "LayShot": [], "PerDef": [], "PaintDef": [], "Stl": [], "ShotTend": [], "ThreeTend": []
            , "MidTend": [], "LayTend": [], "PassTend": []}
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
        dict["PassTend"].append(rand.randint(20, 70))
        
        
    
    return dict




# takes in two team objects, generates players, and assigns them to each team
def initializeTeams(t1, t2):

    players = gen_players(10) # get players

    attributes = ["PlayerID", "Name", "ThreeShot", "MidShot", "LayShot", "PerDef", "PaintDef", "Stl", "ShotTend", "ThreeTend", "MidTend", "LayTend", "PassTend"]

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
def main():

    teamdict = load_teams("knickscavs.json")
    mice = dict_to_team(teamdict["Mice"])
    snakes = dict_to_team(teamdict["Snakes"])

    #mice = Team("Mice")
    #snakes = Team("Snakes")

    #initializeTeams(mice, snakes)



    while True:
        ok = input("press enter to sim, enter anything else to exit")
        if ok == "":
            awesomegame = Match(mice, snakes)
            awesomegame.play()
        else:
            break

    updateAveragePts(mice)
    updateAveragePts(snakes)

    save_teams([mice, snakes])



main()

