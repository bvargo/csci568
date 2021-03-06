/*
#myrandomnumber Tutorial
blprnt@blprnt.com
April, 2010
*/

// this is the Google spreadsheet manager and the id of the spreadsheet that we
// want to populate, along with our Google username & password
SimpleSpreadsheetManager sm;
String sUrl = "t6mq_WLV5c5uj6mUNSryBIA";
String googleUser = GUSER;
String googlePass = GPASS;

// font object
PFont label;

void setup() {
   // this code happens once, right when our sketch is launched
   size(800, 800);
   background(0);
   smooth();

   // initialize font
   label = createFont("Helvetica", 24);

   // get the list of numbers from google
   // int[] numbers = getNumbers();

   // hard-code the list of numbers
   int[] numbers = {19, 69, 43, 15, 23, 89, 19, 54, 69, 4, 13, 37, 66, 8, 78, 67, 32, 76, 13, 87, 42, 23, 32, 88, 21, 4, 2, 61, 99, 43, 59, 13, 42, 18, 60, 19, 81, 17, 36, 94, 42, 67, 18, 42, 9, 4, 72, 43, 64, 97, 32, 7, 14, 78, 21, 19, 72, 69, 2, 16, 87, 67, 42, 55, 7, 26, 81, 19, 88, 67, 78, 26, 33, 12, 39, 88, 72, 83, 37, 28, 81, 57, 77, 77, 23, 6, 37, 57, 67, 42, 40, 57, 17, 95, 28, 96, 73, 67, 52, 20, 99, 71, 37, 42, 17, 39, 47, 17, 1, 37, 15, 25, 97, 37, 17, 69, 39, 64, 47, 79, 33, 5, 37, 93, 14, 97, 66, 77, 36, 27, 64, 12, 25, 84, 83, 29, 52, 25, 43, 23, 98, 79, 6, 3, 42, 72, 17, 47, 2, 1, 77, 69, 57, 86, 69, 74, 97, 35, 25, 21, 61, 57, 93, 17, 45, 35, 12, 26, 60, 75, 11, 8, 1, 41, 12, 53, 77, 42, 66, 55, 47, 46, 55, 26, 27, 6, 52, 72, 27, 15, 1, 84, 81, 56, 74, 33, 77, 4, 7, 66, 24, 93, 55, 64, 97, 66, 74, 64, 73, 17, 17, 23, 97, 73, 37, 72, 41, 76, 6, 87, 66, 54, 77, 65, 83};

   // world's easiest data visualization
   //fill(255, 40);
   //noStroke();
   //for(int i = 0; i < numbers.length; i++) {
   //   ellipse(numbers[i] * 8, width / 2, 8, 8);
   //}

   // drawn both the user random numbers and "real" random numbers below the
   // line of original numbers
   //fill(255, 40);
   //noStroke();
   //// original numbers
   //for(int i = 0; i < numbers.length; i++) {
   //   ellipse(numbers[i] * 8, height / 2, 8, 8);
   //}
   //// a line of random numbers
   //for(int i = 0; i < numbers.length; i++) {
   //   ellipse(ceil(random(0, 99)) * 8, height / 2 + 20, 8, 8);
   //}

   // the user random numbers
   //barGraph(numbers, 100);

   // 6 other random number sets
   //for(int i = 0; i < 6; i++) {
   //   barGraph(getRandomNumbers(225), 100 + ((i + 1) * 130));
   //}

   // draw a grid of the numbers
   colorGrid(numbers, 50, 50, 70);
}

void draw() {
   // this code happens once every frame
}

// make a bar graph of the given numbers at the given y value
void barGraph(int[] nums, float y) {
   // make a frequency list for each number
   int[] counts = new int[100];

   // fill initial frequency with zeros
   for(int i = 0; i < 100; i++) {
      counts[i] = 0;
   }

   // tally counts
   for(int i = 0; i < nums.length; i++) {
      counts[nums[i]]++;
   }

   // draw the graph
   for(int i = 0; i < counts.length; i++) {
      colorMode(HSB);
      fill(counts[i] * 30, 255, 255);
      rect(i * 8, y, 8, -counts[i] * 10);
   }
}

// make a grid for the numbers
// nums is for the numbers
// x and y are for the x and y position
// s is the size for an individual block
void colorGrid(int[] nums, float x, float y, float s) {
   // make a frequence list ofr each number
   int[] counts = new int[100];

   // fill initial frequency with zeros
   for(int i = 0; i < 100; i++) {
      counts[i] = 0;
   }

   // tally counts
   for(int i = 0; i < nums.length; i++) {
      counts[nums[i]]++;
   }

   // move the drawing coordinates to the x,y position specified above
   pushMatrix();
   translate(x, y);

   // draw the grid
   for(int i = 0; i < counts.length; i++) {
      colorMode(HSB);
      fill(counts[i] * 30, 255, 255, counts[i] * 30);
      textAlign(CENTER);
      textFont(label);
      textSize(s / 2);
      text(i, (i % 10) * s, floor(i / 10) * s);
   }

   // restore the original corrdinates
   popMatrix();
}
