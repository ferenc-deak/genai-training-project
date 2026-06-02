import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.scss'],
})
export class App {
  prompt = '';

  ragResponse = '';
  aiResponse = '';

  showAi = false;
  showRag = false;

  loading = false;

  constructor(private http: HttpClient) {}

  combineBothAPICall() {
    this.loading = true;

    this.ragResponse = '';
    this.aiResponse = '';

    this.showAi = false;
    this.showRag = false;

    this.sendAI();
    this.sendRAG();
  }

  sendAI() {
    this.http
      .post<any>('http://127.0.0.1:8000/chat', {
        prompt: this.prompt,
      })
      .subscribe({
        next: (res) => {
          this.aiResponse = res.response;

          setTimeout(() => {
            this.showAi = true;
          }, 1000);

          this.checkDone();
        },
        error: () => {
          this.aiResponse = 'Error calling chat';

          setTimeout(() => {
            this.showAi = true;
          }, 1000);

          this.checkDone();
        },
      });
  }

  sendRAG() {
    this.http
      .post<any>('http://127.0.0.1:8000/ask', {
        question: this.prompt,
      })
      .subscribe({
        next: (res) => {
          this.ragResponse = res.answer || res.response;

          setTimeout(() => {
            this.showRag = true;
          }, 0);

          this.checkDone();
        },
        error: () => {
          this.ragResponse = 'Error calling RAG';

          setTimeout(() => {
            this.showRag = true;
          }, 0);

          this.checkDone();
        },
      });
  }

  private completedRequests = 0;

  private checkDone() {
    this.completedRequests++;

    if (this.completedRequests === 2) {
      this.loading = false;
      this.completedRequests = 0;
    }
  }
}
