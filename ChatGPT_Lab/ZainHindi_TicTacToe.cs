using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        bool playerXTurn = true;//declare bool for X player's turn
        string player = "X";//initiate player to X
        public Form1()
        {
            InitializeComponent();
        }

        private void disableButtons()
        //function that disables all buttons and 
        //enable playAgain button
        {
            box1.Enabled = false;
            box2.Enabled = false;
            box3.Enabled = false;
            box4.Enabled = false;
            box5.Enabled = false;
            box6.Enabled = false;
            box7.Enabled = false;
            box8.Enabled = false;
            box9.Enabled = false;
            playAgain.Enabled = true;
        }

        private void checkWinner()//function that check if there's winning
        {
            if (box1.Text == player && box2.Text == player && box3.Text == player || // check horizontal top
                box4.Text == player && box5.Text == player && box6.Text == player || // check horizontal middle
                box7.Text == player && box8.Text == player && box9.Text == player || // check horizontal bottom
                box1.Text == player && box4.Text == player && box7.Text == player || //check vertical left
                box2.Text == player && box5.Text == player && box8.Text == player || //check vertical middle
                box3.Text == player && box6.Text == player && box9.Text == player || //check vertical right
               box1.Text == player && box5.Text == player && box9.Text == player || // check top left to bottom right
               box3.Text == player && box5.Text == player && box7.Text == player) // check top right to bottom le6ft
            {
                MessageBox.Show($"Player {player} Wins!", "");//show player's winning
                if (playerXTurn)
                {
                    int total = Convert.ToInt32(PlayerXWins.Text) + 1;//increment X winning count
                    PlayerXWins.Text = total.ToString();
                }
                else
                {
                    int total = Convert.ToInt32(playerYWins.Text) + 1;//increment Y winning count
                    playerYWins.Text = total.ToString();
                }
                disableButtons();//disbale buttons after incrementing
            }
            else if (box1.Text != "" && box2.Text != "" && box3.Text != "" &&
              box4.Text != "" && box5.Text != "" && box6.Text != "" &&
              box7.Text != "" && box8.Text != "" && box9.Text != "")
            {//if every box is filled but no winning occured 
                MessageBox.Show("TIE!!!!!!!!", "");//tie occured
                int total = Convert.ToInt32(ties.Text) + 1;//increment tie counter
                ties.Text = total.ToString();
                disableButtons();//disable buttons after incrementing
            }
        }

        private void checkTurn(Button box)//function that determine whose turn it is 
        {
            box.Font = new Font("Arial", 24, FontStyle.Bold);//setting font
            if (playerXTurn)//if bool is true
            {
                playerXTurn = false;//make it false
                player = "O";//next player is O
                box.ForeColor = Color.Firebrick;//color
            }
            else
            {//if bool is false 
                playerXTurn = true;//make it true again
                player = "X";//next player is X
                box.ForeColor = Color.SteelBlue;//color
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {
            this.Close();//close game 
        }

        //Box1
        private void box1_Click(object sender, EventArgs e)
        {
            if (box1.Text == "")//if text box is empty
            {
                box1.Text = player;//place X or O
                checkWinner();//check winning condition
                checkTurn(box1);//switch turn
                playerTurn.Text = $"Player {player}'s turn";//prompt out whose turn it is 
            }
        }

        //Box2
        private void box2_Click(object sender, EventArgs e)
        {
            if (box2.Text == "")
            {
                box2.Text = player;
                checkWinner();
                checkTurn(box2);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box3
        private void box3_Click(object sender, EventArgs e)
        {
            if (box3.Text == "")
            {
                box3.Text = player;
                checkWinner();
                checkTurn(box3);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box4
        private void box4_Click(object sender, EventArgs e)
        {
            if (box4.Text == "")
            {
                box4.Text = player;
                checkWinner();
                checkTurn(box4);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box5
        private void box5_Click(object sender, EventArgs e)
        {
            if (box5.Text == "")
            {
                box5.Text = player;
                checkWinner();
                checkTurn(box5);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box6
        private void box6_Click(object sender, EventArgs e)
        {
            if (box6.Text == "")
            {
                box6.Text = player;
                checkWinner();
                checkTurn(box6);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box7
        private void box7_Click(object sender, EventArgs e)
        {
            if (box7.Text == "")
            {
                box7.Text = player;
                checkWinner();
                checkTurn(box7);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box8
        private void box8_Click(object sender, EventArgs e)
        {
            if (box8.Text == "")
            {
                box8.Text = player;
                checkWinner();
                checkTurn(box8);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        //Box9
        private void box9_Click(object sender, EventArgs e)
        {
            if (box9.Text == "")
            {
                box9.Text = player;
                checkWinner();
                checkTurn(box9);
                playerTurn.Text = $"Player {player}'s turn";
            }
        }

        private void playerTurn_Click(object sender, EventArgs e)
        {

        }

        private void playAgain_Click(object sender, EventArgs e)
        //function that if users click playAgain button
        //reset everything to the initiated settings
        {
            playAgain.Enabled = false;
            box1.Text = "";
            box2.Text = "";
            box3.Text = "";
            box4.Text = "";
            box5.Text = "";
            box6.Text = "";
            box7.Text = "";
            box8.Text = "";
            box9.Text = "";
            box1.Enabled = true;
            box2.Enabled = true;
            box3.Enabled = true;
            box4.Enabled = true;
            box5.Enabled = true;
            box6.Enabled = true;
            box7.Enabled = true;
            box8.Enabled = true;
            box9.Enabled = true;
            playerXTurn = true;
            player = "X";
            playerTurn.Text = $"Player {player}'s turn";
        }
    }
}
