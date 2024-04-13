public class MingChuen_Yap_Player { // extends Player
    int selectAction(int n, int[] myHistory, int[] oppHistory1, int[] oppHistory2) {
        if (n == 0)
            return 0; // start with cooperating
        if (n >= 107)
            return 1; // defect at the last minute

        if (oppHistory1[n-1] == oppHistory2[n-1])
            return oppHistory1[n-1]; //if both players act the same, switch to that action

        int defectioncount = 0;

        for (int i=0; i<3; i++){
            if (oppHistory1[n-1-i] == 1 || oppHistory2[n-1-i] == 1) 
                defectioncount++;
        }

        if(defectioncount == 3)
            return 1; //defect if there has been a defector in the last consecutive 3 rounds

        return 0;
    }
}