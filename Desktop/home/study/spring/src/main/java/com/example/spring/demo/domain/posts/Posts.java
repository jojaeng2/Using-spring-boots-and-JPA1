package com.example.spring.demo.domain.posts;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Posts {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(length = 500, nullable = false)
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String content;

    private String author;

    public Posts() {}

    public Long getId() {return this.id; }

    public String getTitle() { return this.title; }

    public String getContent() { return this.content; }

    public String getAuthor() { return this.author; }

    public static class Builder {
        private String title;
        private String content;
        private String author;

        public Builder title(String title) {
            this.title = title;
            return this;
        }

        public Builder content(String content) {
            this.content = content;
            return this;
        }

        public Builder author(String author) {
            this.author = author;
            return this;
        }

        public Posts build() {
            return new Posts(this);
        }
    }

    private Posts(Builder builder) {
        title = builder.title;
        content = builder.content;
        author = builder.author;
    }

    public static Builder builder() {
        return new Builder();
    }

}
