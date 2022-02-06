package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;

public class MemoryMemberRepositoryTest {
    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    public void save() {
        //given
        Member member = new Member();
        member.setName("spring");

        //when
        repository.save(member);

        //then
        Member result = repository.findById(member.getId()).get();
        assertThat(result).isEqualTo(member);
    }

    @Test
    public void findByName() {
        //given
        Member member = new Member();
        member.setName("spring1");
        repository.save(member);

        //when
        Member result = repository.findByName("spring1").get();
        //then
        assertThat(result).isEqualTo(member);
    }

    @Test
    public void findById() {
        //given
        Member member = new Member();
        member.setName("spring");
        repository.save(member);

        //when
        Member result = repository.findById(1L).get();
        //then
        assertThat(result).isEqualTo(member);
    }

    @Test
    public void findAll() {
        //given

        //when

        //then
    }

}
