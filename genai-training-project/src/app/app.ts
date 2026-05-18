import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

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

  loading = false;

  private completedRequests = 0;

  constructor(private http: HttpClient) {}

  sendRAG() {
    this.http
      .post<any>('http://127.0.0.1:8000/ask', {
        question: this.prompt,
      })
      .subscribe({
        next: (res) => {
          this.ragResponse = res.answer || res.response;
          this.checkDone();
        },
        error: () => {
          this.ragResponse = 'Error calling RAG';
          this.checkDone();
        },
      });
  }

  sendAI() {
    this.http
      .post<any>('http://127.0.0.1:8000/chat', {
        prompt: this.prompt,
      })
      .subscribe({
        next: (res) => {
          this.aiResponse = res.response;
          this.checkDone();
        },
        error: () => {
          this.aiResponse = 'Error calling chat';
          this.checkDone();
        },
      });
  }

  combineBothAPICall() {
    this.loading = true;
    this.ragResponse = '';
    this.aiResponse = '';

    this.completedRequests = 0;

    this.sendRAG();
    this.sendAI();
  }

  private checkDone() {
    this.completedRequests++;

    if (this.completedRequests === 2) {
      this.loading = false;
    }
  }
}
