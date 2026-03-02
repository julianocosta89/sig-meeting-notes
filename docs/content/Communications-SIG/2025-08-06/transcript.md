SIG: Communications SIG
Date: 2025-08-06
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Severin Neumann** 00:22 Lisa! Good morning.
**Lisa Jung** 00:25 Good morning. Hold on one second. I don't know why. Oh, hello!
**Severin Neumann** 00:29 Oh!
**Lisa Jung** 00:31 Sorry I was having some zoom issues.
Have you been.
**Severin Neumann** 00:36 I'm fine. How are you today.
**Lisa Jung** 00:38 Good! Good! I can't believe it's like August already. These.
**Severin Neumann** 00:43 Yeah, yeah, time. Time's flying. Right? So.
**Lisa Jung** 00:47 I'm like, why, why is it so busy in August? Yeah.
**Severin Neumann** 00:51 Yeah, yeah, definitely.
Hey? Antoine, hey? Sophia? Thank you for joining.
**Sophia Solomon** 00:59 Hello! Good morning or afternoon.
**Antoine Toulme** 01:02 Morning.
**Severin Neumann** 01:06 Some.
Okay, I think we can get started. Oh, yeah. Let's give Tiffany a minute to join as well.
**Lisa Jung** 01:21 Give me one second I'll be right back.
**TH Tiffany Hrabusa** 01:26 Sorry I was late.
**Severin Neumann** 01:48 Yeah, let's get started up. Let me see if I can share my screen with you.
Can you see them.
**TH Tiffany Hrabusa** 02:04 Yes.
**Sophia Solomon** 02:04 Yep.
**Severin Neumann** 02:08 Awesome, I added. A few pull requests that we have open as topics. But is there anything else? Has anybody else any topics they'd like to discuss, and maybe let let me know, and I can add them to the agenda as a verbally, or, if you prefer, via chat, and I can copy them in.
If not, let's get started. I just said, pick them based on because they're really complex.
the one I quickly wanted to get some sense on this slide. So so we had the open telemetry and practice session with Alibaba.
Daniel created a blog post. I think it's almost done.
The the only thing I I think that was open is that
there was the idea by, like one of the speakers, to write a little bit more in details about what they talked about during this session.
So I was wondering like.
how do we feel about having 2 or one blog post any
I mean, I would be fine with 2. Let let let me put this out here, but but I don't know if anybody says like, here, let's
let's only have one. But this to just also to share this with you. This is really mostly like.
Hey, we had this talk. And here's the video, right? You see, like, it's not a lot of text. So.
and my understanding is that what book Singh would like do
is like, do do a more detailed presentation on that.
**TH Tiffany Hrabusa** 03:53 Sounds good to me, to to.
**Severin Neumann** 03:55 I've got.
**TH Tiffany Hrabusa** 03:55 Good. This is on my list to review today. I didn't get to it yesterday, so.
**Severin Neumann** 04:01 Yeah, no worries. I I skimmed over it and and and like, did a quick read on it. It's
I think it's just fine. So. So if you have to. Feeling like, Hey, this is good to go, then just merge it.
**TH Tiffany Hrabusa** 04:14 Okay.
**Severin Neumann** 04:15 Yeah.
**TH Tiffany Hrabusa** 04:16 Cool.
**Severin Neumann** 04:22 The next one is the.net, docs. But I think, since Fabricio is not here, I'm also not
sure if he's going to join us today. I don't think so. I think he's
yeah. Let's maybe see May. Maybe he's joining later. Maybe not. Then maybe let's skip this for now.
another topic is the ob docs.
I was working on a lot.
I just wanted to to give a quick update on that since we talked about it last time. So so we created like this one big pull request. And my understanding, at least from the Grafana team, was that like, yeah, the moment we have the ob docs
they will like this will be like the source of truth, for
For for it, and like I mean, Bela will continue to exist right. But like, I think, even like today, there was an announcement of like Bela, 2.5,
which, under the hood builds on top of ob right? So
hopefully, like, they will point to a lot of our documentation at some point
and Mario and I like work through it a lot. So so you see, like, there's a lot of discussions ongoing. There's some
things with Ob that are not yet working. So there's like things like helm charts. I think they're
still working towards getting them merged.
Probably a few other ones.
I think that the question I maybe have.
If we want to merge it at some point, nevertheless, and maybe add.
like a note at the top of all those pages, and say, like, Hey, this is work in progress.
or something like that, so so that we have something to iterate on
or if we just hide a few of the pages for the time being.
and then make them active whenever
like those kinds of things. Land. Yeah, I think that's the 2 the 2 options
just give me a second sum up.
They are some rocks at Dominic story.
Oh, just give me a sec.
Yeah. Any any salt on that, any.
**TH Tiffany Hrabusa** 06:58 Oh, just to clarify when you say that some things are not working. You mean, like code, wise in obit. There's things that are not working, not something related to the docs.
**Severin Neumann** 07:07 No, yeah, and and not even code wise. It's more like,
What did I say? Like something like the help chart? Right? It's more like, it's just not.
Yeah.
**TH Tiffany Hrabusa** 07:19 Wired up.
**Severin Neumann** 07:20 Within the within the open telemetry repositories. Right?
**TH Tiffany Hrabusa** 07:25 Yeah, I think if we're creating individual pages for those things that aren't working, we should just hide them, for now.
**Severin Neumann** 07:32 Yeah, I think, high.
**TH Tiffany Hrabusa** 07:33 Frederick.
**Severin Neumann** 07:34 Then then adding.
**TH Tiffany Hrabusa** 07:35 Better to have that incorrect, incorrect docs or things.
**Severin Neumann** 07:39 Yeah, yeah, yeah. Okay, then, maybe let me. I think there's even like a feature in. I'm not sure if it's Hooker or doxy, then, like where it can say, Hide in talk.
so we can still like look at them and see them like building. But they're just not not generated. Just give me a sec.
**TH Tiffany Hrabusa** 08:08 Right.
**Severin Neumann** 08:10 It's bad time in their life.
yeah. Okay. So so I will continue working on that. I I hope that I get it into a shape that we maybe can merge it by the end of the week, because I will be away like the next 2 weeks
we would be great just to have this landed, if not like. I would have to postpone this after after I'm back. So yeah. But but I think this is going to be like a
a huge huge milestone, because, like, I think, this is going to add like
a a big chunk of documentation. And it also looks like Bela or Ob. How it is called. Now it's like a project. People are like super excited about so.
**TH Tiffany Hrabusa** 08:57 Yup on the Bayla side of things. Just a quick update. Internally, people at Grafana are meeting and the direction that we're hoping to take the Bayla documentation in is basically more like Grafana specific use cases. And so we'll leave, like the ob documentation to be like the the technical source of truth. But
we're still working that out. So.
**Severin Neumann** 09:25 Okay, okay.
okay, yeah. But but that's good. Right? So so that that we get this out of the way. Yeah, perfect.
Yeah, I said I. I think that's like a big milestone to have to migrate it over, and in that case it was really easy, because, like those use who go who go under the hood so so it was
fairly straightforward to to get all those things migrated. Yeah, awesome.
Yeah. The other one is about the language maintainers. I created this
a week ago, or something like that.
I said, this is this is more thought, as like an experiment.
That we allow some languages to merge their own Prs right? I think.
at the end. Just let's maybe give it a try. And then I think the only thing like maybe we should agree on like for how long we want to like run this as an experiment that we say like, Hey, in in 3 months from now. Let's recheck in and and and have a have a discussion on that.
**TH Tiffany Hrabusa** 10:49 Yeah, I think with Pto. It probably more than a few weeks right? Like, with every.
**Severin Neumann** 10:53 Yeah, definitely. I mean.
initially, I also was like, Hey, let's do it for a month. But then I was like, yeah.
things things very often take, take a lot longer.
So yeah, I have to. Yeah.
**TH Tiffany Hrabusa** 11:10 Maybe end of September, so like about 2 months.
I don't know if that.
**Severin Neumann** 11:20 Yeah, that's not even more. That's a little bit more than a month. It's more like
2 months, but also not too long. Yeah, yeah, it's a good idea. Yeah.
okay, so so what's also part of that, I think we also need to see, like, who of the approvals we are going to to move into the Maintainers Group.
But then I think we're good to go.
I said I wanted to focus it on Japanese and Portuguese at the beginning, because they're the most active. That does not mean like that. We not later enable that for other languages as well.
I I mean one discussion. That's like, probably one we we have to continue
is around like, Hey, do we want to have one group of localization maintainers or one per language.
I still lean towards having one. Localization maintainers group
but because at the end it's less about.
hey? Is this correct in my language? It's more around like, Hey, is this correct in the sense of how we want to build
build out the localization? So but also, I think that's not something we need to decide right now.
**TH Tiffany Hrabusa** 12:33 Yeah, it may also come down to what they are willing to do like. Will they be willing to take on the work of
a maintainer for all of the localizations versus just their own.
**Severin Neumann** 12:48 Yeah, exactly. So. So my hope really is that there's like.
just like at some point, I mean, how the other language like like would like the
the other 6 have a like. They have their contract maintainers, and they have their like core maintainers. And this is kind of our contract situation like I mean in
in in an ideal world, they would live in their own repository. Right? But
that that's not something we maybe
are not doing at some point but
but right now it's more around like having people that take the responsibility on right? So but yeah, let's see. So so then let's maybe I I see that I maybe merge this at some point and see who we move into the Maintainers Group
and then we give it a go and monitor it for the next few weeks.
Stuff!
net docs, as said,
this is also really cool, because Fabricio also like
took a lot of like the docs that they have in.net, which you just can see like it's like a lot
and and turn them into into something like
or thenet, seek to live in our repository. I think the discussion we have to have at some point is to make sure that thenet maintainers then, like continue doing their docs there versus like in the repository
but since Fabricio is not here today, we can. We can take this offline?
But yeah, another like, major major thing, I'm I'm excited about yeah.
A few topics from my side. Any
anything anybody wants to talk about
Lisa. We still owe you a review of your work, I guess.
Yeah.
Let me see if I can find some time for that.
it's like, yeah, yes, the script.
I will take a look. Yeah.
**Lisa Jung** 15:06 Thank you.
**Severin Neumann** 15:12 Awesome beyond that, I said. I mentally, already like trying to get a lot of things out of my system, because it will be on Pto. The next 2 weeks, but also will miss the next big meeting.
Yeah.
Anything else.
**TH Tiffany Hrabusa** 15:31 I don't have anything today.
**Severin Neumann** 15:34 Cool, and thank you everybody for joining. And
oh, Sophia, you wanted to say anything.
**Sophia Solomon** 15:41 Oh, I just wanted to say, before you go on, Pto, we could talk, maybe outside of this meeting about like the reference app, and like the.
**Severin Neumann** 15:50 Oh, yeah. Oh, yeah, I know. I mean, we have another like
30 40 min. So so I'm always happy to talk about that one?
So yeah, they can.
Honestly.
the the thing with that project is like, I would love to spend much, much more time on it. But like it's it's always slipping through the cracks. So
So let me let me find it.
so so so the moment I how how I think about it right now is that like?
And I think this is already in a really good shape. So so the thing is like that we
land this document?
So if you have any time to to also like, take take a look at into that.
And I said, this is more like a specification how the application should look like, and how it should be
instrumented.
that we, the moment we merge it, that we like distributed among the language seeks and say like, Hey.
can you implement that and own that, and and then see like how? And that's probably a little bit of a work right there. There are definitely also need people to help me with like to to reach out to to a bunch of maintainers and say, like, Hey, this is what we want to do. Can you? Can you work with us? Or can you create an an issue for that
and attach and help wanted to it, and and then we we can work on that. I think that's like the next steps. So if you want to help with that, I think step one is. And even if you're not yet like
member of the hotel org, or even like involved in
in in in any roles you can take a look at that and just write a comment like looks good to me, or comment on it, or something like that. Right? So so this is already like
really helpful. If if people people take a look.
**Sophia Solomon** 17:46 Got it. Okay.
**Severin Neumann** 17:48 Yeah, maybe because I yeah, delay, yeah.
**Sophia Solomon** 17:53 No sorry. Go ahead, oh, awesome!
So we want to put this out into the other, like the language Sigs.
**Severin Neumann** 18:06 Exactly. Yeah.
**Sophia Solomon** 18:08 News. Okay.
**Severin Neumann** 18:10 We had an idea of like which languages we wanted to reach first.st That's why we also have here.
I laugh from now I'm blanking ruby.
We had Choi, I mean he stopped net rust. He! He does multiple languages. We definitely have some the folks from go and and javascript on that. So so, yeah, but but that's more, something like
and and where we also need them, people help implementing that. So the moment the 6 they're like, Hey, this is cool. Let's have it in this and that repository, and this and that folder.
It's very likely that they will not be the 1st persons, people to implement it. So this is also an opportunity to say, like, Oh, I'm good at Language X, let me implement that in in this and that language right?
So yeah, that's at least how it, how it goes in my head.
**Sophia Solomon** 19:03 Okay, that, yeah, that makes sense.
**Severin Neumann** 19:06 Yeah. So maybe let's do that. Maybe you take another look into that. I mean, I have now a few people looking into that.
Let me know how how you like it, how it looks like. And this goes also to to have anybody else in this call. Right? If you have a few minutes, and and can take a look at this Pr. And if you think like it looks good, then maybe we finally merge it.
and then it'll be like distributed among the the different language. 6. And then I guess, like a lot of them from them will come back and say like, hey? I don't like the way you're doing that, and then may maybe we have to to reiterate on that one. I'm
I'm well aware of that. But yeah, normally, it's like, Hey, we, we have something. And then, like we can, we can discuss that.
**Sophia Solomon** 19:48 Okay, okay. So next steps, distributing it to going over and then distributing it to the.
**Severin Neumann** 19:55 Yeah, exactly. So so I can. I can maybe maybe do the distribution. But then I also need people to monitor it and help me like with the with the engagement, because, like, there's like, how many languages do we have? 9, 11, something like that?
So so there's like a good set of of 6. We we then need to interact right.
**Sophia Solomon** 20:17 Okay.
If you're gonna send it out, then I'd love to help coordinate. I know python and Javascript really well, but.
**Severin Neumann** 20:25 Okay, that's good to know.
Awesome.
**Sophia Solomon** 20:35 That's all for me.
**Severin Neumann** 20:37 Awesome. Thank you.
**Sophia Solomon** 20:38 Me!
**Severin Neumann** 20:43 Anything else
awesome. Then I wish you a great rest of your day.
and talk to you in 4 weeks from now, or in, of course, on slack talk to you. Bye, bye.
**Lisa Jung** 21:06 Great time. Off. Bye, everybody.
**Severin Neumann** 21:08 Bye.
