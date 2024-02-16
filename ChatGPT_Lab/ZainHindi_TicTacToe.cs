using System;
using System.Drawing;
using System.Windows.Forms;

namespace TicTacToe
{
    public partial class Form1 : Form
    {
        private bool _playerXTurn = true;
        private string _player = "X";

        public Form1()
        {
            InitializeComponent();
        }

        // Disables all buttons on the form except the "playAgain" button.
        private void DisableButtons() =>
            Controls.OfType<Button>().ToList().ForEach(button => button.Enabled = false);

        // Checks if there is a winner by iterating through all possible winning lines.
        private void CheckWinner()
        {
            foreach (var line in WinningLines())
                if (line[0].Text == _player && line[1].Text == _player && line[2].Text == _player)
                {
                    MessageBox.Show($"Player {_player} Wins!", "");
                    UpdateScore();
                    DisableButtons();
                    return;
                }

            // If there is no winner and all buttons are filled, it's a tie.
            if (IsTie())
            {
                MessageBox.Show("TIE!!!!!!!!", "");
                ties.Text = (int.Parse(ties.Text) + 1).ToString();
                DisableButtons();
            }
        }

        // Switches turns between players and updates the display accordingly.
        private void CheckTurn(Button box)
        {
            box.Font = new Font("Arial", 24, FontStyle.Bold);
            box.ForeColor = _playerXTurn ? Color.Firebrick : Color.SteelBlue;
            _playerXTurn = !_playerXTurn;
            _player = _playerXTurn ? "X" : "O";
            playerTurn.Text = $"Player {_player}'s turn";
        }

        // Handles click events on the tic-tac-toe buttons.
        private void BoxClick(object sender, EventArgs e)
        {
            var box = (Button)sender;
            if (box.Text == "")
            {
                box.Text = _player;
                CheckWinner();
                CheckTurn(box);
            }
        }

        // Updates the score label of the current player.
        private void UpdateScore() =>
            (playerXTurn ? PlayerXWins : playerYWins).Text = (int.Parse(playerXTurn ? PlayerXWins.Text : playerYWins.Text) + 1).ToString();

        // Resets the game state for a new round.
        private void playAgain_Click(object sender, EventArgs e)
        {
            Controls.OfType<Button>().ToList().ForEach(button =>
            {
                button.Text = "";
                button.Enabled = true;
            });

            _playerXTurn = true;
            _player = "X";
            playerTurn.Text = $"Player {_player}'s turn";
            playAgain.Enabled = false;
        }

        // Checks if all buttons are filled, indicating a tie.
        private bool IsTie() => Controls.OfType<Button>().All(button => button.Text != "");

        // Defines all possible winning combinations in tic-tac-toe.
        private Button[][] WinningLines() =>
            new Button[][]
            {
                new Button[] { box1, box2, box3 }, // Horizontal top
                new Button[] { box4, box5, box6 }, // Horizontal middle
                new Button[] { box7, box8, box9 }, // Horizontal bottom
                new Button[] { box1, box4, box7 }, // Vertical left
                new Button[] { box2, box5, box8 }, // Vertical middle
                new Button[] { box3, box6, box9 }, // Vertical right
                new Button[] { box1, box5, box9 }, // Top left to bottom right
                new Button[] { box3, box5, box7 }  // Top right to bottom left
            };
    }
}
