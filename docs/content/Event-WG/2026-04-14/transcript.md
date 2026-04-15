SIG: Event WG
Date: 2026-04-14
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:52 Hello! Hi, Robert.
**Robert Pająk (@pellared)** 00:56 Hello, hello, I'm good, I'm just… just also after a meeting.
That's not sick meeting, so yeah, easier for me.
How are you?
**Liudmila Molkova** 01:11 Oh, I'm… I'm fine, I'm… Be tired, too.
have a lot of things going on, and one of the things that I'm delivering some crazy 3-hour-long workshop next week.
In Barcelona, and it's been quite a bit of, effort to prepare. This is Mario, by the way, the Mario Marcias?
Yeah, yeah. From Obi, yeah.
**Robert Pająk (@pellared)** 01:37 Yeah.
So, you're going… you're doing the… if it's Mario in Barcelona? Because Mario is… What is… he's living in Austria?
**Liudmila Molkova** 01:45 He's in Barcelona!
**Robert Pająk (@pellared)** 01:47 He's in Barcelona?
**Liudmila Molkova** 01:48 Yeah.
Why are your t-shirt?
**Robert Pająk (@pellared)** 01:54 Excuse me, t-shirt?
Also.
**Liudmila Molkova** 01:56 Yeah, or have you got it?
**Robert Pająk (@pellared)** 01:58 from this KubeCon.
This is our Splunk.
Orthopa.
**Liudmila Molkova** 02:02 Oh!
Was it available at the booth?
**Robert Pająk (@pellared)** 02:07 Yes, it was.
**Liudmila Molkova** 02:09 Oh, shit.
I missed such a great opportunity!
**Robert Pająk (@pellared)** 02:15 Yeah.
We usually have already rated t-shirts and coupons.
**Liudmila Molkova** 02:22 Okay.
**Robert Pająk (@pellared)** 02:24 I tried to collect all the phrases.
**Liudmila Molkova** 02:28 That was the previous one.
**Robert Pająk (@pellared)** 02:29 I think each coupon, we try to have one new world, so I think the last one was, Rock, I Am Your Father, which I had during my presentation.
you came to the right trace, I think it was, like, 3 years ago?
**Liudmila Molkova** 02:45 Oh…
**Robert Pająk (@pellared)** 02:47 observability is kind of, yeah, just, you know, from the words, it's just but yeah, still a t-shirt. I don't remember the others, but they were also.
**Liudmila Molkova** 02:58 Is there a Polish word for observability?
**Robert Pająk (@pellared)** 03:02 There is…
**Liudmila Molkova** 03:05 But is it…
**Robert Pająk (@pellared)** 03:06 I think it's upset of… I would object this is a… Observe about it?
So, for value.
**Liudmila Molkova** 03:13 I've recently heard, seen someone.
**Robert Pająk (@pellared)** 03:17 Yes, Observovalmerscht. Observablet.
**Liudmila Molkova** 03:21 Okay, at least it's…
**Robert Pająk (@pellared)** 03:22 coming from automation.
So, it's, you know, from… so it's not brand new for IT, it was before.
**Liudmila Molkova** 03:30 Yeah. In Russian, this is crazy, I've… it's a stupid idea to translate terms. Oh, sorry, I shouldn't have it on the recorded call, but it's an interesting idea to translate common terms into language-specific, like, the Thread is a good example. You cannot, you should not translate thread.
But observability is called Nablo Diamasht.
Like, something you could see… But it, it, it sounded so weird to me, anyway.
**Robert Pająk (@pellared)** 04:00 We are making fun right now with our Polish colleagues, we are trying to make the Polish translation, and also vocabulary, and yeah, there are so many funny works coming up, but we are enjoying it. But we try to… we try to be the translation legit, but because it's so, you know, it's not utilized, usually.
But what is funny, that I know that there are some people in Poland, some startups, which are very, you know, Polish, they're only Polish working for Polish companies, and I know that some people really use Polish IT words, and they are not using the English words.
like, for instance, they do not use, I create a Git branch, they do, they say GAONG. Which is a branch, a literal branch, you know, in Polish words. So, yeah, there are people who are using these words.
**Liudmila Molkova** 04:47 Yeah.
**Robert Pająk (@pellared)** 04:47 We can start slowly.
Rudomua, do you want to drive today?
**Liudmila Molkova** 04:55 Yeah, I can drive, I… we don't really have any agenda, though.
**Robert Pająk (@pellared)** 05:02 Maybe we can copy the last one. I even have not opened.
doc.
**Liudmila Molkova** 05:10 Yeah, so the only thing I came to my mind that There is a thread somewhere in semantic conventions, let me try to pull it up, About structured stack traces, and… Florian mentioned that they have structured stack traces for .
**Robert Pająk (@pellared)** 05:38 Florence, Java.
**Liudmila Molkova** 05:39 filing.
Profiling.
**Robert Pająk (@pellared)** 05:41 Piling, okay.
**Liudmila Molkova** 05:44 And… Since they have structures that traces there.
And we want cross-signal things, and we've been discussing structured Stack traces cautiously.
for at least some cases, maybe we should go and investigate what profiling does for the structures like traces and… if… We can leverage something from it.
**Trask Stalnaker** 06:15 Yeah, we did actually, look at that when we did the code.method.name… stuff.
To align with that.
With the profiling definition of what is a method what was it? Method name, or method…
**Robert Pająk (@pellared)** 06:40 Yes, dysfunctioning.
**Trask Stalnaker** 06:42 Forget.
**Robert Pająk (@pellared)** 06:43 Technical.
**Trask Stalnaker** 06:43 Yeah.
**Robert Pająk (@pellared)** 06:44 I'm leaving.
**Trask Stalnaker** 06:46 Whether it includes… The class, or…
**Robert Pająk (@pellared)** 06:50 Beautiful.
**Trask Stalnaker** 06:50 Stuff like that.
But yeah, I like it. I mean, I think the only… I think we've always sort of intended to have structured stack traces someday, And… I think it's just… it's… Waiting on somebody who has the motivation and time to do that.
**Liudmila Molkova** 07:17 Yeah, motivation and time is a good constraint.
**Robert Pająk (@pellared)** 07:21 Yeah.
**Liudmila Molkova** 07:27 Okay, let's bring back… do we… I think this, this is… we agreed upon. There is nothing actionable in this one.
**Robert Pająk (@pellared)** 07:36 Yeah, it's on my to-do.
**Liudmila Molkova** 07:38 Okay.
**Robert Pająk (@pellared)** 07:39 Probably tomorrow morning.
**Liudmila Molkova** 07:41 Yeah, it's actionable, it does not need a discussion. That's probably the right frame.
**Robert Pająk (@pellared)** 07:45 Yeah.
Second one as well, I think it just needs reviews.
I, I think I addressed today's, I think I already made a comment that changed may be in SDK or conflict, I changed to shield being SDK, because I also had a feeling that Jack wanted to have it, like, kind of out of the box, so I even changed it to a shield.
**Trask Stalnaker** 08:13 Cool, I like that.
**Liudmila Molkova** 08:31 Must do nothing.
**Robert Pająk (@pellared)** 08:38 Yes.
**Liudmila Molkova** 08:42 So, if this is a specialized processor, the Excel log record.
If it matches, if it can be translated to Spanish and translates it.
Otherwise, it does nothing.
Do we care about the chaining? Is it… it's not a… It's not a chain… it is a chain processor. It's not.
Huh.
**Robert Pająk (@pellared)** 09:08 instance.
**Liudmila Molkova** 09:11 Okay, so you would fork.
Before.
**Robert Pająk (@pellared)** 09:15 Exactly.
**Liudmila Molkova** 09:36 Alright.
No parameters.
**Trask Stalnaker** 09:43 Nice and simple.
**Liudmila Molkova** 09:45 Yep.
Oh, and is it… is it exp… is it development now?
**Robert Pająk (@pellared)** 09:56 I hope so.
**Liudmila Molkova** 09:58 Yep, it is.
Wonderful.
I mean, we can target merging it by the end of the week. I think we have… All the approvals, and it's not something that would break anybody, and it's in development.
Let's… maybe…
**Robert Pająk (@pellared)** 10:57 Open a sec, let's opened the door.
**Liudmila Molkova** 11:11 Okay… Easy!
Oh, Trask, did you want to review? Do you have… would you have time by the end of the week? Or did you already approve it?
**Trask Stalnaker** 11:33 I already approved it. Oh, nice.
**Liudmila Molkova** 11:35 Awesome.
Okay…
**Robert Pająk (@pellared)** 11:41 How was your birthday?
For this one, for triaging.
by the GC or PC, just to have it as accepted.
**Liudmila Molkova** 11:52 Oh, I see.
The triage will happen, the TC triage will happen tomorrow, but it's not in the TC inbox. I think there is a multiple staff triage, and it should arrive in the TC inbox. I can bring it to the agenda for the TC call tomorrow.
**Robert Pająk (@pellared)** 12:08 Yeah, I think it's better for TTC than the GC.
It comes with your kids.
**Liudmila Molkova** 12:22 Anything interesting?
**Robert Pająk (@pellared)** 12:25 Do you want to prototype already, or it's not muted yet?
**Liudmila Molkova** 12:33 finisher.
**Robert Pająk (@pellared)** 12:34 Yes, it doesn't…
**Liudmila Molkova** 12:36 Different decorations.
**Robert Pająk (@pellared)** 12:37 Okay.
**Liudmila Molkova** 12:45 I… I'm going to waste a little bit more of your time by just typing in the TC call, otherwise I'm not sure if I will remember.
**Robert Pająk (@pellared)** 12:59 It's fine.
**Trask Stalnaker** 13:01 That's what these meetings are for. Dedicated time to do the stuff that we would otherwise forget about.
**Robert Pająk (@pellared)** 13:09 Exactly.
**Liudmila Molkova** 13:14 I learned it from you, Trask, that actually, Yeah.
Let's just review PRs and do the boring stuff. Not everything needs to be a discussion.
**Robert Pająk (@pellared)** 13:36 Are there any other topics?
Insecure, the system.
**Liudmila Molkova** 13:54 No other topics from… Me?
**Trask Stalnaker** 14:11 Nothing…
**Liudmila Molkova** 14:12 Yay!
**Trask Stalnaker** 14:13 Yeah.
Job done.
**Robert Pająk (@pellared)** 14:22 Awesome.
**Liudmila Molkova** 14:22 Great to see you!
**Trask Stalnaker** 14:24 See y'all.
