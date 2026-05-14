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
  response = '';
  loading = false;

  constructor(private http: HttpClient) {}

  send() {
    this.loading = true;
    this.response = '';

    this.http
      .post<any>('http://127.0.0.1:8000/chat', {
        prompt: this.prompt,
      })
      .subscribe({
        next: (res) => {
          this.response = res.response;
          this.loading = false;
        },
        error: () => {
          this.response = 'Error calling chat';
          this.loading = false;
        },
      });
  }

  sendRAG() {
    this.loading = true;
    this.response = '';

    this.http
      .post<any>('http://127.0.0.1:8000/ask', {
        question: this.prompt, // ✅ FIXED
      })
      .subscribe({
        next: (res) => {
          this.response = res.answer || res.response;
          this.loading = false;
        },
        error: () => {
          this.response = 'Error calling RAG';
          this.loading = false;
        },
      });
  }
}
