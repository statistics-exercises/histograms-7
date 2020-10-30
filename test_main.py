import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        for i in range(5) :
            x, y = fighand.patches[i].get_xy() 
            self.assertTrue( np.fabs(x+0.5*fighand.patches[i].get_width()-i)<1e-7, "the x-coordinates of the bars in your histogram are incorrect" )
            
    def test_normalised(self) : 
        ssum = 0.
        fighand=plt.gca()
        for i in range(5) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram has not been normalised" )

    def test_plot(self) :
        fighand=plt.gca()
        for i in range(5) :
            bar = np.sqrt( probs[i]*(1-probs[i]) )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( fighand.patches[i].get_height() - probs[i] )<bar, "the heights of the bars in your histgoram appear to be incorrect" )
