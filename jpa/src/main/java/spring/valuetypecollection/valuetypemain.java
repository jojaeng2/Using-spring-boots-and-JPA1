package spring.valuetypecollection;

import org.springframework.boot.autoconfigure.SpringBootApplication;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

@SpringBootApplication
public class valuetypemain {


    public static void main(String[] args) {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpabook");

        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();

        try {
            tx.begin();

            Member2 member = new Member2();

            // 임베디드 값 타입
            member.setHomeAddress1(new Address1("통영", "몽돌해수욕장", "660-123"));

            // 기본값 타입 컬렉션
            member.getFavoriteFoods().add("짬뽕");
            member.getFavoriteFoods().add("짜장");
            member.getFavoriteFoods().add("탕수육");

            // 임베디드 값 타입 컬렉션
            member.getAddress1History().add(new Address1("서울", "강남", "123-123"));
            member.getAddress1History().add(new Address1("서울", "강북", "000-000"));

            em.persist(member);

            tx.commit();

        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();

    }
}
