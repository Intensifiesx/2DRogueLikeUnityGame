#include<pthread.h>
#include<semaphore.h>
#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>

sem_t tobacco, paper, matches, smoked;
void* agent(void *data) {
    while (1) {
	switch (rand() % 3) {
	case 0:
	    /* Missing tobacco */
	    sem_post(&paper); 
	    sem_post(&matches);
	    printf("Agent places [ ] Tobacco [X] Paper [X] Matches\n");
	    break;
	case 1:
	    /* Missing paper */
	    sem_post(&tobacco);
	    sem_post(&matches);
	    printf("Agent places [X] Tobacco [ ] Paper [X] Matches\n");
	    break;
	case 2:
	    /* Missing matches */
	    sem_post(&tobacco);
	    sem_post(&paper);
	    printf("Agent places [X] Tobacco [X] Paper [ ] Matches\n");
	    break;
	default:
	    printf("Error!\n");
	    exit(-1);
	}

	/* Wait for the smoker to signal they're done */
	sem_wait(&smoked);
	printf("Agent has been signaled a smoker is done\n");
	sleep(3);
    }
}

void* terry(void *data) { // terry consumer 
    while(1) { // wait n smoke forever wassup
        if(sem_trywait(&paper) == 0){ // if paper available, grab it and enter the condition
            if(sem_trywait(&matches) == 0){ // if matches available, grab it enter the condition
                printf("Terry takes the paper and matches, rolls a cigarette and smokes it\n"); //print smoker specific message
                sleep(3); // ensure no print interruptions
                sem_post(&smoked); // signal agent the smoker smoked 
            } else {
                sem_post(&paper); // if not both available put back the paper 
            }
        }
    }
}

void* prascilla(void *data) { // prascilla consumer 
    while(1) { // wait n smoke forever wassup
        if(sem_trywait(&tobacco) == 0){ // if tobacco available, grab it enter the condition        
            if(sem_trywait(&matches) == 0){ // if matches available, grab it enter the condition
                printf("Prascilla takes the tobacco and matches, rolls a cigarette and smokes it\n"); //print smoker specific message
                sleep(3); // ensure no print interruptions
                sem_post(&smoked); // signal agent the smoker smoked 
            } else {
                sem_post(&tobacco); // if not both available put back the tobacco 
            }
        }
    }
}

void* marge(void *data) { // marge consumer 
    while(1) { // wait n smoke forever wassup
        if(sem_trywait(&tobacco) == 0){ // if tobacco available, grab it enter the condition
            if(sem_trywait(&paper) == 0){ // if paper available, grab it enter the condition
                printf("Marge takes the tobacco and paper, rolls a cigarette and smokes it\n"); //print smoker specific message
                sleep(3); // ensure no print interruptions
                sem_post(&smoked); // signal agent the smoker smoked 
            } else {
                sem_post(&tobacco); // if not both available put back the tobacco 
            }
        }
    }
}


int main(int argc, char** argv) {
    sem_init(&tobacco, 0, 0);
    sem_init(&paper, 0, 0);
    sem_init(&matches, 0, 0);
    sem_init(&smoked, 0, 0);    
    srand(getpid());
    
    pthread_t t;
    pthread_create(&t, NULL, terry, NULL); // terry was born to smoke
    
    pthread_t p;
    pthread_create(&p, NULL, prascilla, NULL); // prascilla was born to smoke
    
    pthread_t m;
    pthread_create(&m, NULL, marge, NULL); // marge was born to smoke
    
    pthread_t a;
    pthread_create(&a, NULL, agent, NULL); 
    

    pthread_join(a, NULL);
    pthread_join(t, NULL);
    pthread_join(p, NULL);
    pthread_join(m, NULL);
    return 0;
}