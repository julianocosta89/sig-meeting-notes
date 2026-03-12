SIG: Developer Experience SIG Meeting
Date: 2025-07-23
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:10 Hey, Tristan? Just a second I forgot my water.
**tristan** 00:15 Good.
Hmm.
**Juliano Costa | Datadog** 02:16 Hello! Hello!
**tristan** 02:20 Second.
**Damien Mathieu** 02:39 Hey! Good morning!
**Juliano Costa | Datadog** 02:41 You know.
**tristan** 03:01 Oops!
Getting sick kids.
**Juliano Costa | Datadog** 03:10 Oh, tell me about it! Last week was busy.
It's impressive how how they care helps.
**tristan** 03:28 Daycare getting one in school soon. Hopefully.
The well, yes, that daycare gets you sick, doesn't it?
So? Yeah.
**Juliano Costa | Datadog** 03:44 No So from my end I have no updates.
I haven't heard back from from Asado. I I said I I would ping them again.
I'm not sure if I for do that, or I have a contact. I have.
And I know someone that works at Langfuse.
I know that they are a small company.
I don't know how big is their deployment.
I was there. I was there back in November last year.
They they hosted a meetup, and I went there to present, and we chatted a bit.
They do Llm.
Observability and something, but I know that they use hotel I'm I'm gonna reach out to them and see if they they are willing to to jump in a call and talk a little bit about their their deployment. I believe they would be like very small
**tristan** 05:06 Good.
**Juliano Costa | Datadog** 05:08 Good they they would fit the small company, and well, I I can, of course, reach out to to mastodon again. But it it's a bit tricky with them because they are a small team, and they they manage the whole thing. And yeah, it's so.
**Damien Mathieu** 05:29 Maybe. It's possible that because it's the summer we're just on vacation.
Though I see that has some github contributions yesterday and on Monday. But I don't know.
**Juliano Costa | Datadog** 05:45 I know. Yeah, replied to me, and he pointed me to team Tim is the the engineer that is responsible for deploying the collector and managing it so but I haven't heard back from from team. But I know sad. That team would be like busy and stuff. So yeah.
**tristan** 06:10 Summer too.
**Damien Mathieu** 06:15 By the way, on that subject, I will be out from like the 1st 3 weeks of August.
**tristan** 06:22 Yeah, you could.
**Juliano Costa | Datadog** 06:26 Me. I I believe me, too. I haven't booked my my holidays yet, but whenever I do I'll let you guys know.
**tristan** 06:36 Always Canada work that way.
We need more, the except, yeah, I'm leaving my current job and taking time. So I we'll have more time for this, I guess, so I'll be working on the blog post. It won't be working working so we can get started on the it.
Once we wanna publish second and hopefully find the small company soon and get those ready, and they'll be ready to go once we have the the small one and they get it'll help with writing the small one quicker. Because, yeah.
you know, some idea of how to structure and all that.
**Juliano Costa | Datadog** 07:24 Cool. Okay.
so you you mentioned that it would ideally, we would publish small medium and large,
**tristan** 07:37 They can. You know we don't have to.
**Juliano Costa | Datadog** 07:44 And in in the way that we have. Now we have small medium, or we have small and 2 large ones right.
**tristan** 07:53 It is.
**Juliano Costa | Datadog** 07:54 Or.
**tristan** 07:55 This guy's.
**Juliano Costa | Datadog** 07:55 Lesson is even larger, sorry.
**tristan** 07:57 Well, the skyscanner is smaller than Atlassian. Yeah.
**Juliano Costa | Datadog** 08:00 Yeah.
**tristan** 08:01 Yeah, I was thinking they might be 2. Yeah, we might need a better medium.
Hmm, I'm not sure you're I have. Do you remember how many nodes they have.
**Juliano Costa | Datadog** 08:19 No, but I know that they have like. I think they have 3 or 4 different types of collector that they deploy. Well, it's recorded. So I can revisit. But they they have a couple of different types of collectors that they deploy.
**tristan** 08:36 Right.
**Juliano Costa | Datadog** 08:37 It's not like simple setup, so to say.
**tristan** 08:50 View.
Yeah, pretty sure. Atlassing is larger.
because they're in the tens of thousands.
Lectures.
**Juliano Costa | Datadog** 09:06 I do have notes on that one sec.
Awesome.
They have a total of 1,400.
**tristan** 09:22 1,400, okay.
**Juliano Costa | Datadog** 09:24 1,400 employees.
**tristan** 09:29 It could be wouldn't be bad to have a hundred or something size company.
**Juliano Costa | Datadog** 09:40 And I found out that they they use the they use the contribut.
**tristan** 09:45 Yeah.
**Juliano Costa | Datadog** 09:47 Over. Oh, yeah, it was a nice finding.
**tristan** 09:51 Yeah. Yeah. Got your blog post.
**Juliano Costa | Datadog** 09:54 Yeah, they had some interesting kind of not?
Well, they had some interesting bumps during the the process. One that I want to share here is that 4 0 4 was tracked as errors.
and they had 100% sampling for errors. So they were getting a lot of spends that were error. But the 4 4 was from from a cache.
So it's not actually an error. So they had to kind of use the filter processor there, and they saved a lot of money when they did it.
So fine.
**tristan** 10:45 There being a debate at a time, I guess I guess it stayed as on here.
Yeah, I can't. I'll have to look back at the could have swore it wouldn't have been in there.
It was a long debate when that was 1st defined in the spec.
That's that's annoying.
That 4 4, for a lot of reasons, could not be in here.
Hmm, yeah, I can imagine.
And.
**Juliano Costa | Datadog** 11:27 Another thing that it? Yeah, no. Go ahead.
**tristan** 11:30 No, I was just gonna say you'd also pick up anybody trying to just spam the the endpoints with fake stuff to overload. So you just pick all those up with 4 0. Fours. Of made up pages, so that'd be annoying.
What what are you gonna say?
**Juliano Costa | Datadog** 11:50 Oh, another thing that is interesting from them is that they use fluentbeat for logs.
**tristan** 11:56 Yep.
**Juliano Costa | Datadog** 11:56 That's because it was there before, and they have never revisited.
And and I when I when I when I was wrapping up the interview, I asked, Hey, have you ever considered using fluentbeat for traces, metrics and logs like kind of playing the the To to the other team? And he was like, no, we haven't. But yeah, I think when when they started with Flintbeat, Flintbeat only supported logs, and when they started with all the collector, the collector only supported traces. So it's like, now they have this.
**tristan** 12:38 And.
**Juliano Costa | Datadog** 12:39 Makes the environment.
**tristan** 12:41 Oh, yeah.
**Juliano Costa | Datadog** 12:46 Because now both of them support both.
**tristan** 12:48 Yeah.
**Juliano Costa | Datadog** 12:49 So we do so I I think as I said to to you, Tristan, and just to keep them in on the loop. I I can write the sky scanner. Story.
I have all the the content I can go through. I won't promise to do this like this week or next week, but I'll I'll do it.
**tristan** 13:16 And I can do it.
**Juliano Costa | Datadog** 13:19 Then we we see, but of course, and What was his name? I forgot.
**tristan** 13:30 Neil.
**Juliano Costa | Datadog** 13:31 Neil. Yeah. Neil said that he he would kind of redact some stuff from from their collector config, and then send the auto beaming to us.
**tristan** 13:41 Nice. Okay.
Perfect.
**Juliano Costa | Datadog** 13:44 So we can add to the to the blog post as well. I think it's a valid.
**tristan** 13:52 Good.
**Juliano Costa | Datadog** 13:54 Evil to have. Yeah.
**tristan** 13:56 Cool.
**Juliano Costa | Datadog** 14:05 Then, yeah, I'll I'll let you guys know whenever I hear back from from infuse.
**tristan** 14:12 Yeah, yeah. And I have a potential medium that I should check on. See what size their deployment is. And so I'll get back in the Channel about that.
**Juliano Costa | Datadog** 14:24 Awesome.
**tristan** 14:25 Okay, cool. You can call here. Okay.
Thank you.
**Juliano Costa | Datadog** 14:32 See you guys.
**tristan** 14:33 Bye.
**Juliano Costa | Datadog** 14:34 But.
