SIG: Go Auto-Instrumentation SIG
Date: 2026-01-20
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/tIFHmNlbztwq5LWwjU9zS78gPcbx2ODoHTeTL6lL97Kq5yAEyupMrizV7OYjGASx.Z8mk9Le-76kHLF9L
============================================================

## Zoom Recording Transcript

**Tyler** 00:18 Hey, Raphael.
**Rafael Roquetto** 00:22 Hey, how's it going?
**Tyler** 00:24 Good, good, long time to see.
**Rafael Roquetto** 00:26 Yeah, yeah, Happy New Year!
**Tyler** 00:28 Happy New Year? Yeah, yeah. How was the vacation?
**Rafael Roquetto** 00:31 Yeah, it was awesome. It was warm, I had the beach, it was green. How about yours?
**Tyler** 00:37 Yeah, it was pretty good. I stuck around here, so it was not as nice as that. Where did you go? I can't remember.
**Rafael Roquetto** 00:42 Brazil.
**Tyler** 00:44 Oh, that's right. Okay, yeah, I remember you telling me that, yeah. Yeah. Yeah, that sounds way nicer than, cold Portland, Oregon. Yeah.
**Rafael Roquetto** 00:51 Yeah, yeah, it's, yeah, it was pretty good. I mean, now I have to go on a diet, because I'm probably 5 kilos.
better, but… yeah.
It's a good way to start the year, and reset the mind.
**Tyler** 01:04 Yeah, no, that's good. Were you down there, seeing family, or just vacation? Yeah.
**Rafael Roquetto** 01:09 Yeah, yeah, my family, so, like, 5 weeks. That was… it was good. For the most part, it was good. There were some… some… some days were really, really warm, really hot, I'm not used to that anymore.
**Tyler** 01:19 Oh, yes.
**Rafael Roquetto** 01:20 no AC, but I'm not gonna complain, you know?
**Tyler** 01:23 What's really warm? Is that, like, 34 or something like that?
**Rafael Roquetto** 01:26 Yeah, 34, 36, but it's… at the beach, it was really, really humid.
**Tyler** 01:30 So it can get a bit…
**Rafael Roquetto** 01:32 oppressive, I guess, the heat.
**Tyler** 01:35 Yeah, oh yeah.
**Rafael Roquetto** 01:36 Then you go to the pool and drink beer, and it's fine.
**Tyler** 01:39 Yeah, that's always a good option. It's funny you didn't have any AC, though, that's gonna be a little rough there, yeah.
Yeah.
**Rafael Roquetto** 01:48 Yeah. But… It's fine.
**Tyler** 01:50 Yeah, it's always like, no AC in January, and you're like, oh man, like, that's, not what you expect.
**Rafael Roquetto** 01:55 The problem with Brazil is that people have this mindset that, oh yeah, it doesn't snow here, for the most part, or it doesn't get that hot, so we have mild climate, so we don't need AC or heating, but in practice, you feel cold during winter, and you feel hot during summer, and…
**Tyler** 02:13 Yeah, yeah. I gotcha. Gotcha.
Yeah, I'm looking at the meeting notes.
**Bhupinder Singh** 02:24 Bye, guys.
**Tyler** 02:27 Hey, how's it going?
**Bhupinder Singh** 02:29 Good cook.
**Tyler** 02:33 It doesn't look like there's been a lot on the agenda lately.
But yeah, if you guys wanted to add your name to Pinder and Rafael.
And then… yeah, we can wait a little bit. I don't know if we're gonna have any topics to discuss.
I know that I've been working more in the OB space lately, and other spaces. Yeah. Yeah.
**Rafael Roquetto** 02:59 Yeah, for my part, I don't have much. I'm just, like, sliding back into work, start working on… on this, selling… oh, I know it's a ghostig, but since we're waiting for people. On OB, we have this, issue where we sometimes inject a transparent header where it already exists, or when it already exists, because it's been externally injected.
So, I'm just looking to that now, just to…
**Tyler** 03:25 Mmm.
**Rafael Roquetto** 03:25 get the brain fired back, hopefully get a PR this week.
**Tyler** 03:29 Oh, that's interesting.
I wonder if I've seen this.
Yeah I feel like I was playing… so I was playing with, This, like, distributed trace context, like, chain stuff there, and trying to, like, get some testing… in, like, the wrong place. I need to get… move this testing into, like, the actual OB code, but, like, Yeah, it was… it was actually, it was cool. I did… I did find that, like, you could go across, like, 8 different languages, and it worked, which was, you know, really impressive. There was definitely some, like, the .NET stuff was a little bit of a restriction.
And in playing with the .NET, like.
prior to .NET 9, I added, like, the agent, the hotel agent there.
And, yeah, like, sometimes the traces would be connected, and sometimes they wouldn't.
**Rafael Roquetto** 04:20 Hmm.
**Tyler** 04:20 Also rust. Rust is, like, somewhat flaky, but, like.
I told people that it actually worked, and they were very surprised that it even worked, so, but anyways, like… Yeah, I was like, I kind of wonder why it's flaky, though. I wonder if this is the reason, like, they were… they had a trace parent, like, we were just overriding it, so… but yeah.
**Rafael Roquetto** 04:40 For Rust, if… I mean… I don't know, I guess… Unless we… we have some, like… code explicit for Rust that I don't think we do. I think what happens from the top of my mind, it tries to correlate context using, you know, threads, But I used…
**Tyler** 05:01 Yeah. And if Rust is anything like C++.
**Rafael Roquetto** 05:05 You know, that, that, that will… that's not a… It's…
**Tyler** 05:10 Yeah, so…
**Rafael Roquetto** 05:11 Guaranteed, right?
**Tyler** 05:12 I kind of cheated, so I was more interested to see if it would work, so I wrote both my C++ app and my Rust app to be as single-threaded as I could make them, which is… I'm sure there were edge cases I missed, but like, yeah, so that was exact… that was exactly the approach I used, just to see if it, like.
it could be done, but yeah, I mean, like… Yeah, that… nobody's gonna actually write their code the way I wrote it, so… Yeah. But I just wanted to, like, double check and see, like, if there was something else, yeah. Because, like, the .NET one was interesting, because I, like, I tried to do that as well there.
Yeah, good luck, trying to… to override, like, the HTTP handler to, like, be single-threaded. It was, like… just not possible. In fact, like, I ended up looking at, like, just writing raw TCP at some point, and I was just like, well, this isn't gonna work either, so… The answer I found out was just upgrade.
Yeah, the answer actually was kind of interesting, because I was talking with Nicola about this. We were going really into the weeds at this point, but no one else is here, so whatever.
But, like, I was talking to Nikola, and, like, he was saying that, like, in theory, we should be able to make it work for .NET 9 and 10, or 9 and plus, and I just upgraded and it worked. And then I was like, huh, what's, like, I don't know… I don't know, maybe he meant that, and, like.
what he didn't know either, and so I was talking with, Robert, a guy on my team, about Because he's really knowledgeable about .NET, and, like, apparently .NET has always supported, like, trace context propagation in their, like, native, like, backend. It's just that, like, prior to .NET 9, they were doing it in a non-W3C, like, format.
So, like, that actually already exists there, and so when I mentioned that to Nikola, he's like, oh, that and what we could probably do for… that is just use the wrong format in the prior versions, and then make it work there as well, and I was like, oh, huh, that's interesting. Yeah, so… yeah, there was, like, a lot of really interesting edge cases there that I… I don't know. I found, yeah.
**Rafael Roquetto** 07:12 Yeah, Nikola mentioned something yesterday, I think he's sick today, haven't spoken to him, about that, and he said, like, what we could do with OB is… On ingress, we can… if there is no transparent header, we can inject that.
into the HTTP payload, and then the .NET would… would just propagate it seamlessly, so we don't have to do anything. Right. So that's… that's on my list. We'll see how… how that play out.
**Tyler** 07:44 Yeah, I… I mean, I don't know all of the details, so, like, don't blame me if I'm completely wrong about that, but, like, this is just, like, what I've gathered through all the people that are smarter than me in .NET, so, yeah.
**Rafael Roquetto** 07:55 Yeah. But…
**Tyler** 07:57 Yeah, yeah, some cool stuff.
**Rafael Roquetto** 08:00 Yeah, I'm excited to be back.
**Tyler** 08:03 Yeah, cool, what are we at? 8 minutes in?
Hmm, I don't think we're gonna have many other folks attending.
So, I think we could probably end it here. We could definitely talk more about, oh, yeah, about… Obi goals. I don't know if you have a chance, Raphael, to maybe take a look at last week's meeting. Notes for Obi, for the, other stuff? Like, yeah.
**Rafael Roquetto** 08:27 It's huge.
**Tyler** 08:28 Yeah, so I'm trying to get those into, like, issues today, so we can go over it again tomorrow, and just kind of, like, organize our thoughts around that.
it seems a little ambitious for me, right now to get that all done today, but I'm gonna try. And then, yeah, so if you haven't yet, yeah, if you've already taken a look, cool, then we'll talk about it tomorrow. So, yeah.
**Rafael Roquetto** 08:49 Okay, yeah, I skipped a bit. I have to go and read it. Like, yesterday was catching up with everything after 5 weeks, but I'll take a look again today. If there is anything that I see worth mentioning, I'll Slack you. Otherwise.
**Tyler** 09:02 Or, yeah, yeah, or, yeah, like, especially things that, like, you don't see on there.
**Rafael Roquetto** 09:07 Okay.
**Tyler** 09:08 that you think we should probably try to focus on this upcoming year. So, yeah, just kind of heads up on that one, yeah.
**Rafael Roquetto** 09:13 Alright, yeah, sounds good.
**Tyler** 09:15 Cool.
Alright, well, we can, in this, Today, and then, yeah, talk to you in the EVPF Instrumentation sig, so…
**Rafael Roquetto** 09:25 Thank you. See you guys. Bye.
**Bhupinder Singh** 09:28 Good luck.
