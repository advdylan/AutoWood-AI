import unittest
from board_based_optimizer import Board, format_fit_check


class TestFormatFitCheck(unittest.TestCase):
    def setUp(self):
        # Set up test cases for Board objects
        self.board1 = Board(X=1000, Y=500, occupied=False)
        self.board2 = Board(X=800, Y=600, occupied=False)
        self.board3 = Board(X=500, Y=500, occupied=True)  # Occupied board

    def test_single_board_fits(self):
        # Test single board where format fits
        self.assertTrue(format_fit_check(self.board1, 400, 200))
    
    def test_single_board_does_not_fit(self):
        # Test single board where format does not fit
        self.assertFalse(format_fit_check(self.board1, 1200, 600))

    def test_multiple_boards_one_fits(self):
        # Test list of boards where one board fits
        boards = [self.board1, self.board2, self.board3]
        self.assertTrue(format_fit_check(boards, 700, 400))

    def test_multiple_boards_none_fit(self):
        # Test list of boards where no board fits
        boards = [self.board1, self.board2, self.board3]
        self.assertFalse(format_fit_check(boards, 1200, 700))

    def test_invalid_input(self):
        # Test invalid input
        with self.assertRaises(TypeError):
            format_fit_check("invalid input", 400, 200)

if __name__ == '__main__':
    unittest.main()
