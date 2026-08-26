SIG: CI/CD SemConv SIG
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Neil Yashinsky** 02:57 Hey there, Alan. How's it going?
**Alan Clucas (Pipekit Inc)** 03:01 I'm alright.
How are you?
I wasn't sure anyone was going to turn up.
**Neil Yashinsky** 03:07 Oh, sorry, one more time?
**Alan Clucas (Pipekit Inc)** 03:08 I wasn't sure anyone was going to turn up, so I just drifted off.
**Neil Yashinsky** 03:12 Yeah, I'll give you a brief glance at my face. I forgot to put on my makeup this morning, but I feel like a little social pressure. Hello.
I'm a camera off kind of guy for various reasons, but, you know, there's, like, it's fun, to, like, connect with people.
That's honestly one of my favorite things about OTEL. You know, we work across a lot of different companies and we have a lot of different perspectives accordingly.
But everyone, by and large, is kind of committed to the community.
We might see that differently, what that means exactly, but, you know, that commitment is real, and it means something, and it's… I think it motivates… collaboration in a real sense, and so that's, you know, that's who I am, I think, at my core in some ways.
**Alan Clucas (Pipekit Inc)** 03:57 Yeah, I mean, my, I, I… I was around for… Linux pre-version 1.
**Neil Yashinsky** 04:04 Mmm.
**Alan Clucas (Pipekit Inc)** 04:05 Really?
**Neil Yashinsky** 04:05 Oh, man. Alright, now we're gonna have to have, like, a stop coffee chat or whatever. Tales from Alan!
**Alan Clucas (Pipekit Inc)** 04:13 No, not really. I mean, I remember my first encounter with Linux was.
Somebody had put Linux on one of the… machines in the computer room at uni, and I booted up and went, what's this? And went and got my DOS boot disk. It was the fastest machine in the lab, and then I could run Fractant really well on that machine.
**Neil Yashinsky** 04:35 the.
**Alan Clucas (Pipekit Inc)** 04:36 But but by by the end of that year, I was I was a convert and being an evangelist. I remember being at my first company, I was an evangelist for Linux, and eventually they after I left, they produced Linux products, but their first thing was like I wanted to run I wanted to run Linux on my desktop, and so yeah, they said which one we can go and buy Red Hat CDs.
**Neil Yashinsky** 04:57 but.
**Alan Clucas (Pipekit Inc)** 04:58 When Red Hat was properly free.
**Neil Yashinsky** 05:00 So.
**Alan Clucas (Pipekit Inc)** 05:01 They bought three of them so that they could install it on three machines. And I tried to explain that this was like, that's not how this works. You only need one CD. No, we're going to buy three CDs.
**Neil Yashinsky** 05:09 I mean, I suppose in some ways it's a nice, supportive thing to do these days, but yeah, no, funny. I would say you could probably just buy 3 licenses just as easily, or whatever. There wasn't even a license to buy, was there?
**Alan Clucas (Pipekit Inc)** 05:21 There was no license to buy it.
**Neil Yashinsky** 05:22 Yeah, this is.
**Alan Clucas (Pipekit Inc)** 05:24 That was when Red Hat was completely… the GPL thing before CentOS, and…
**Neil Yashinsky** 05:29 Maybe.
**Alan Clucas (Pipekit Inc)** 05:30 Yeah, whatever.
**Neil Yashinsky** 05:31 Discs or whatever, they're building a discotheque in the back room or something.
**Alan Clucas (Pipekit Inc)** 05:35 Right.
**Neil Yashinsky** 05:36 you.
**Alan Clucas (Pipekit Inc)** 05:36 But, yeah, so, I mean, actually, my full-time job is open source, on the Argo side mostly, but, it's like… I'm really glad I've managed to find a place doing that, so…
**Neil Yashinsky** 05:48 Yeah, yeah, that's great. I mean, especially these days, it's, it's really interesting timing, I think, to be, doing, if you will, computing or, you know, software work or whatever, and… It seems like, you know, double-edged sword. Like, some people are being… finding very productive ways to work, and some people who are incredibly talented, I'm sure you hear about them all the time, are really struggling to find the right, you know, situation, and… It's so hard to believe anything the media talks about around stuff like this, and job laws, and things like that, but… Yeah, I think we can kind of just get a sense from, like, talking to our colleagues and whatnot.
That's what I trust most.
**Alan Clucas (Pipekit Inc)** 06:27 Yeah, yeah, it's a… it's a tough time. I wouldn't… I wouldn't… I was quite glad when my son… my son's just about to start, like.
**Neil Yashinsky** 06:34 I.
**Alan Clucas (Pipekit Inc)** 06:34 A new phase in education.
Before pre-university, and he he decided he wasn't gonna do computer science, and it was like, yeah, that's that's the right call at this point.
**Neil Yashinsky** 06:44 I'm.
**Alan Clucas (Pipekit Inc)** 06:45 Not sure where it's going to be in a few years time. Yeah, for sure.
**Neil Yashinsky** 06:49 Yeah, would be nice to catch up on that more, but hello, Carlos, looks like Carlos joined, so Carlos, how's it going?
**Carlos Alberto Cortez** 06:57 Hey, we have nothing in the agenda, and I saw that most people cannot make it today. I think that that's kind of standard stuff for Europe, that people are taking holidays.
**Neil Yashinsky** 07:06 Yeah.
**Carlos Alberto Cortez** 07:08 So, very quiet weeks. But yeah, I think that both Edrin and Christophe will be back full power next week. I think this week they're back, but they need to catch up with… Yeah.
Other stuff, yeah.
**Alan Clucas (Pipekit Inc)** 07:21 Yeah.
I won't be around next week, I've got nothing at all to report, I was just showing up to… See what… see what was happening. Yeah. Yeah.
**Neil Yashinsky** 07:33 I guess same, not that I didn't think anybody was expecting me to do anything, but, yeah. Well, I mean, we can always, go back to chatting about what Alan's son has in the future, or maybe we'll just, we'll just, break here, and then, I don't know, see you in another week or two.
Depending on… Your summer vacations?
**Carlos Alberto Cortez** 07:51 Yeah, from my side, I am very packed, like, trying to work on many things that.
**Neil Yashinsky** 07:58 Yeah, yeah.
**Carlos Alberto Cortez** 07:58 I will, so it's up to you, but yeah, other… if there's nothing to talk on the technical side, I will just drop out.
**Neil Yashinsky** 08:03 Yeah, let's give everybody some time back. That's like the easiest decision we can all make, and hopefully we'll catch up soon and we'll be rested and or more productive or both.
**Carlos Alberto Cortez** 08:12 Yeah, correct, yeah, I think that, yeah, yeah. So let's see. Yeah, in the meantime, I guess that, yeah, there's nothing pending, but.
If there's something, just don't forget to write that down so we can discuss that once we have the full team back.
**Neil Yashinsky** 08:27 Great!
**Alan Clucas (Pipekit Inc)** 08:27 All right. See you next time. Ciao.
**Neil Yashinsky** 08:29 Yeah, thanks for your leadership. Yes, excellent. Very well done. Very well done. Take care, everyone.
**Carlos Alberto Cortez** 08:33 Heads out.
**Neil Yashinsky** 08:34 Take care, bye.
