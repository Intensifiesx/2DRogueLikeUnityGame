#include<pthread.h>
#include<semaphore.h>
#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>

sem_t sem_tobacco, sem_paper, sem_matches, agent_ready;
pthread_mutex_t lock;
pthread_cond_t cond_smokers[3]; // Condition variables for smokers

// Enum for readability
enum { TOBACCO, PAPER, MATCHES, NUM_ITEMS };

// Smoker function
void* smoker(void *arg) {
    int my_items = *(int*)arg;
    while (1) {
        pthread_mutex_lock(&lock);
        // Wait for the right combination of items
        pthread_cond_wait(&cond_smokers[my_items], &lock);

        // Smoker specific logic
        printf("%s takes their items, rolls a cigarette and smokes it\n", (my_items == TOBACCO) ? "Terry" : (my_items == PAPER) ? "Prascilla" : "Marge");
        sleep(3); // Simulate smoking time

        // Signal the agent that smoking is done
        sem_post(&agent_ready);

        pthread_mutex_unlock(&lock);
    }
}

// Agent function
void* agent(void *data) {
    static int items[] = { TOBACCO, PAPER, MATCHES };
    while (1) {
        sem_wait(&agent_ready);

        pthread_mutex_lock(&lock);
        int missing_item = rand() % NUM_ITEMS;

        // Notify the appropriate smoker
        printf("Agent places items missing %d\n", missing_item);
        pthread_cond_signal(&cond_smokers[missing_item]);

        pthread_mutex_unlock(&lock);
        sleep(1); // Simulate time taken to place items
    }
}

int main(int argc, char** argv) {
    sem_init(&sem_tobacco, 0, 0);
    sem_init(&sem_paper, 0, 0);
    sem_init(&sem_matches, 0, 0);
    sem_init(&agent_ready, 0, 1); // Start with agent ready
    pthread_mutex_init(&lock, NULL);
    for (int i = 0; i < NUM_ITEMS; i++) {
        pthread_cond_init(&cond_smokers[i], NULL);
    }

    srand(time(NULL));
    pthread_t smoker_threads[NUM_ITEMS], agent_thread;
    int smoker_ids[NUM_ITEMS] = {TOBACCO, PAPER, MATCHES};

    // Create smoker threads
    for (int i = 0; i < NUM_ITEMS; i++) {
        pthread_create(&smoker_threads[i], NULL, smoker, &smoker_ids[i]);
    }

    // Create agent thread
    pthread_create(&agent_thread, NULL, agent, NULL);

    // Wait for threads to finish (they won't, in this setup)
    pthread_join(agent_thread, NULL);
    for (int i = 0; i < NUM_ITEMS; i++) {
        pthread_join(smoker_threads[i], NULL);
    }

    return 0;
}