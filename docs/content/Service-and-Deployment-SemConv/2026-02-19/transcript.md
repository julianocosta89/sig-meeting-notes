SIG: Service and Deployment SemConv
Date: 2026-02-19
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Ankit** 05:07 Hi. Hello, Rashid.
**Yoshi Yamaguchi** 05:09 Hi, Ankit, how are you?
**Ankit** 05:11 I'm good, how you doing?
**Yoshi Yamaguchi** 05:13 Good, good. Do you hear me well? I'm, I'm attending on the, conference now, and then on the boost duty, so… Maybe you hear a lot of noises around me.
**Ankit** 05:22 It's fine, yeah, I can hear you nice. I think you have good noise cancellation earphones.
**Yoshi Yamaguchi** 05:28 Awesome. Appreciate it.
Cool.
**Ankit** 05:32 Do we have other people joining? Or I can just, tell you about this proposal that we had discussed in the last, US time meeting, Pacific time meeting.
Yeah, I…
**Yoshi Yamaguchi** 05:43 I appreciate if you can give you a debrief of the discussion in last week.
**Ankit** 05:50 Right, so I had presented a proposal about this business.costcenter.id attribute that we're planning to add. So it's, like, related to, mostly for finance ops management. We see this attribute already being used there for multiple cloud providers, and also being used in the observability platforms as well. It's just that everything is manual right now, all the tools normalize the kind of cost center attributes that are already there. So, we are trying to formalize that, have a common convention.
I had initially proposed business.cost center, but then during the discussion, in that meeting, it panned out that we should do it, costcenter.id, so that we are open to adding more sub-attributes in the future as well. So, I think everyone was aligned on .id, so now I have updated the proposal to costcenter.id.
**Yoshi Yamaguchi** 06:42 So… So is the ID going to be, arbitrary string type, or is it going to be more, like, numeric?
**Ankit** 06:50 It's going to be a string.
**Yoshi Yamaguchi** 06:52 Okay, that'd be great, that'd be great. As long as… as long as the ID and, Coastal Center distributes are in string type, then I'm totally… I agree with defining, you know, setting these labels into the standard that's asked… into the standard. So, yeah, I'm… I'm really positive.
On your, on your, on your proposal.
**Ankit** 07:17 Awesome. So I'll be visiting a PR for that soon. While we are here, I'm also planning to add the other one. It's called service.businessUnit. So, do you foresee any concerns for that? I am yet to share a proposal for that. I am still on the works. I'll probably share it by end of day.
**Yoshi Yamaguchi** 07:37 Oh… Can you repeat the name of the label?
**Ankit** 07:43 Business… business unit.
**Yoshi Yamaguchi** 07:46 Business unit, is it?
**Ankit** 07:47 Yes, yes, yes. Service.businessUnit.
**Yoshi Yamaguchi** 07:50 Is it… is it on a GitHub, or are there any documents for it?
**Ankit** 07:56 I do have a document, but it's being internally reviewed with my team.
**Yoshi Yamaguchi** 08:00 Watch it, I see.
**Ankit** 08:01 So, I can just share it, yeah.
I'll attach it in the meeting notes, after we meet.
**Yoshi Yamaguchi** 08:07 Bye.
**Ankit** 08:09 Yeah, I guess we can have that discussion in the next meeting.
**Yoshi Yamaguchi** 08:12 percentage. I see, I see, I see.
**Ankit** 08:14 Yeah.
**Yoshi Yamaguchi** 08:16 Yeah, that makes sense.
I mean, the initial makes sense, so… Sounds good.
**Ankit** 08:22 Yeah, I mean, it's similar to kind of cost center. The discussion is almost the same. We see the same fragmentation, and we need the same kind of standardization.
**Yoshi Yamaguchi** 08:33 Right.
Cool.
Yeah.
**Ankit** 08:41 Yep.
**Yoshi Yamaguchi** 08:42 Yeah, regarding these two proposals, I'm totally positive, and I'm totally supportive to introducing both of them into the standards, so… yeah.
**Ankit** 08:54 Awesome.
Do you speak Japanese, by the way.
**Yoshi Yamaguchi** 08:59 Yeah, of course, because I'm a native Japanese speaker, so…
**Ankit** 09:01 I got that from the accent, like, I learned Japanese for 6 months.
added the name, and then you also had the exercise, like, I should ask. Awesome.
**Yoshi Yamaguchi** 09:11 If you… if you'd like to, like, try your Japanese here, then I can… I can talk in Japanese as well.
**Ankit** 09:19 But no, it's very bad right now, because I learned it 3 years back, so it has been a long time. And I didn't practice it, of course, as I never moved to Japan.
**Yoshi Yamaguchi** 09:31 Okay, then you can resume learning Japanese again, so that we can talk in Japanese.
**Ankit** 09:37 Definitely.
**Yoshi Yamaguchi** 09:40 Yeah, yeah, yeah.
Cool, cool.
Do you have any other topics now?
**Ankit** 09:46 No, I don't. I was just talking to Ayushi, so she… she did say she's joining, and she might have something to discuss. I don't know if she should wait, or… Give me a sec, I'll just call her once.
To see if she's joining. Yeah, thank you.
**Yoshi Yamaguchi** 10:42 Thanks.
**Ankit** 10:57 Yeah, she's still stuck in Bangalore traffic.
She planned to be at 11?
**Yoshi Yamaguchi** 11:03 But the.
**Ankit** 11:03 Traffic is so crazy right now, so she can't make it. So yeah.
**Yoshi Yamaguchi** 11:08 I have… I have eaten the bungalow once, and then I know how toastrick is bad there, so… Yeah, I mean, it takes me half an hour for just a 2km,
**Ankit** 11:19 We've transit to my office, so it's really bad.
So, yeah, I guess then we don't have anything more to discuss from this angle.
**Yoshi Yamaguchi** 11:29 Awesome. So then, yeah, once you, I, put the thumb up on your… A proposal for, A coastal center?
And also, once you, submit another proposal, like, I mean, GitHub issue regarding the business unit, let me know. I put some up as well.
**Ankit** 11:51 Stop, stir. Thank you.
**Yoshi Yamaguchi** 11:52 Cool. Alright.
Boom.
Ben, I'll give you 20 minutes back.
**Ankit** 11:59 Thank you.
**Yoshi Yamaguchi** 12:01 Altemos!
**Ankit** 12:03 Bye.
Right.
