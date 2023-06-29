class Score:
    score = 0
    score_for_apple = 100
    score_for_time = 1
    total_frames = 0
    frames_to_decrease_score = 60
    color = 'orange'

    def update_score(self):
        self.total_frames += 1
        if not self.total_frames % self.frames_to_decrease_score:
            self.score -= self.score_for_time

    def get_score(self):
        return self.score

    def apple_eaten(self):
        self.score += self.score_for_apple
        self.score_for_apple += 5
