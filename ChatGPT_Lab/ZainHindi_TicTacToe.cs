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

        private void DisableButtons()
        {
            foreach (Control control in Controls)
            {
                if (control is Button button)
                {
                    button.Enabled = false;
                }
            }
            playAgain.Enabled = true;
        }

        private void CheckWinner()
        {
            foreach (var line in WinningLines())
            {
                if (line[0].Text == _player && line[1].Text == _player && line[2].Text == _player)
                {
                    MessageBox.Show($"Player {_player} Wins!", "");
                    UpdateScore();
                    DisableButtons();
                    return;
                }
            }

            if (IsTie())
            {
                MessageBox.Show("TIE!!!!!!!!", "");
                ties.Text = (int.Parse(ties.Text) + 1).ToString();
                DisableButtons();
                return;
            }
        }

        private void CheckTurn(Button box)
        {
            box.Font = new Font("Arial", 24, FontStyle.Bold);
            box.ForeColor = _playerXTurn ? Color.Firebrick : Color.SteelBlue;
            _playerXTurn = !_playerXTurn;
            _player = _playerXTurn ? "X" : "O";
            playerTurn.Text = $"Player {_player}'s turn";
        }

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

        private void UpdateScore()
        {
            var scoreLabel = _playerXTurn ? PlayerXWins : playerYWins;
            scoreLabel.Text = (int.Parse(scoreLabel.Text) + 1).ToString();
        }

        private void playAgain_Click(object sender, EventArgs e)
        {
            foreach (Control control in Controls)
            {
                if (control is Button button)
                {
                    button.Text = "";
                    button.Enabled = true;
                }
            }
            _playerXTurn = true;
            _player = "X";
            playerTurn.Text = $"Player {_player}'s turn";
            playAgain.Enabled = false;
        }

        private bool IsTie()
        {
            foreach (Control control in Controls)
            {
                if (control is Button button && button.Text == "")
                {
                    return false;
                }
            }
            return true;
        }

        private Button[][] WinningLines()
        {
            return new Button[][]
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
}
