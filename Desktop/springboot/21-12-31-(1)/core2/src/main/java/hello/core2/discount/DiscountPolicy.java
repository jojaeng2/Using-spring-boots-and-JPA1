package hello.core2.discount;

import hello.core2.member.Member;

public interface DiscountPolicy {

    int discount(Member member, int price);
}
