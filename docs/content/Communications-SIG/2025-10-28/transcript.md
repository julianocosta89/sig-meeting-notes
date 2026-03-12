SIG: Communications SIG
Date: 2025-10-28
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 01:47 Hello there.
**Patrice CNCF** 01:57 Hello, hello.
**Vitor Vasconcellos** 02:00 Just checking out of it.
**Patrice CNCF** 02:01 Good, I'm good, how are you?
**Vitor Vasconcellos** 02:04 Unlimited, too.
What do you use for your camera that moves when you move, too? Is that a software, or is there something from the camera?
**Patrice CNCF** 02:18 It's… I think it's… macOS and iOS since the latest version.
kind of… than that. There's a mode called, hey.
What's it called? Let me… let me see… it's called Center Stage.
**Vitor Vasconcellos** 02:36 Okay, I will take a look at it.
It will be very useful for any…
**Patrice CNCF** 02:45 Yeah, it's useful when I'm… I'm not… Mid-frame, so… the Mac will just… Put me mid-frame and fix the lighting, kind of.
No.
**Vitor Vasconcellos** 02:58 Oh, I didn't know this feature.
That's interesting.
**Patrice CNCF** 03:05 Hello, everybody!
**Severin Neumann** 03:07 Hello, hello?
I think we don't have to wait for… A lot more people, but maybe let's give everybody a little bit.
I think Fabricio and Tiffany are still in Berlin for the… Conference? Write to Docs? Right to Docs, I think it's called.
Yeah. Yeah. So they're probably not joining?
Just give me a sec. No, I think we can get started.
I can share my screen. I put a few things on the agenda, just to have a few things on the agenda, but… Whatever comes to your mind, we can also spend some time on that.
Let me see that I shared the right thing… I hope you can see this just well.
Yeah.
I thought I'd just bring up a few… Of the blog posts that we.
**Patrice CNCF** 04:14 Question before we go on, is it one of us who turned on transcription?
**Severin Neumann** 04:20 Maybe me, let me see… Meeting is being true.
**Patrice CNCF** 04:26 We've been having AI agents coming up on… willing…
**Severin Neumann** 04:31 I think… I think that's a… I think that's something that… so I get from CNCF meetings those emails from time to time into the, in the governance committee mailbox.
Maybe it's misconfigured. Because, like, if the transcripts are turned… No, but is there not a difference between the transcripts and the AI whatever? I think transcript is just that it just generates a text version of whatever we said, versus, like, this AI summary.
Okay, fine.
**Patrice CNCF** 05:07 In both cases, there's AI involved, but if we're okay with trans… transcription…
**Severin Neumann** 05:15 I… I have… yeah, I mean, I don't know, we can… technically, we can turn it off if we think it's not a good thing to have, but…
**Patrice CNCF** 05:23 No, it's fine, I just wanted to make sure it wasn't one of those issues, like the Otter AI showing up without us asking.
**Severin Neumann** 05:29 Yeah, no, I think that would look different, right? That the person turns their dream back.
**MG Marylia Gutierrez** 05:33 Yeah, they usually show as an actual, like, person on the call, and they start recording, so you.
**Severin Neumann** 05:39 Kick, kick.
**MG Marylia Gutierrez** 05:40 them out.
**Severin Neumann** 05:44 Yeah.
Yeah, I can look at the… at the transcript right now, live. That's funny. I think you even can use it for real-time translation or something like that already, or… yeah, whatever.
**Patrice CNCF** 05:57 Oh, let's do that. Let's all speak in our native language and, see how…
**Severin Neumann** 06:01 See how to swim.
**Patrice CNCF** 06:02 Universal Translator works.
**MG Marylia Gutierrez** 06:05 Yeah, it's usually, like, pretty, pretty bad, like, Portuguese. There's, like, yeah, there's some weird, weird stuff. One time, we had, like, a call, and every single time, it translated, like, Kubernetes to a different thing, so it was, like, Cuban Daddies, and then all over, so yeah, it was some weird thing.
**Severin Neumann** 06:26 Yeah, okay, thanks. Give it some time, but maybe in a year from now, we can all speak our native language, and… like, the lip-sync, like, even do some AI with our mouse, that it, like, looks different for everybody, and I, like… Then I speak perfect Portuguese and everything, I'm looking forward to that.
Anyways, let's quickly… I said, for the blocks, it's more like, hey, I just wanted to quickly have… Have a summary on that.
We have that one blog on the unroll component. There's not a lot that needs to be said. I think Collector Stick is taking a look.
The more important one is this one, because this is, like, graduation related.
I'm not sure if anybody of you attended the spec meeting that happened, like, An hour ago?
thing… Austin… I unfortunately could only get a little bit of it, but, like, I think Austin presented it there, so… We wanted to put out this blog post, To call out, like.
Kind of a plan around stability and a few of the things that came out.
In the… in the… in the review around, like, hey, this is what… what hotel needs.
To… to accomplish certain goals for, like, graduation.
So that thing is kind of important.
I think the goal is to send it out early next week, or something like that. I'm unfortunately out next week, so if anybody can help them to finalize that, it would be really good.
Just to… to have some attention to that.
**MG Marylia Gutierrez** 08:11 Yeah, so that one, I was a little confused by his thing, because a lot of people are adding comments already on the post, so it's like, I want feedback on the blog itself, but then after, also, more feedback, so I wasn't sure, like, how much he wanted to keep the PR up.
But, yeah, if he gives.
**Severin Neumann** 08:29 Yeah, I think what…
**MG Marylia Gutierrez** 08:29 next week.
**Severin Neumann** 08:30 Yeah, yeah, I think the idea was that, like, all the maintainers can review it. So review it as a maintainer and member of the community, that's the one thing, but of course, at some point, we also need to do the review of, like, style and copy editing and whatever, and see, like, hey.
**MG Marylia Gutierrez** 08:47 Yeah.
**Severin Neumann** 08:47 Pit, right?
Or those minor things about, like, That is still in the draft status, and there's, like, a few things that just… context-wise need to be done. I try to… to throw in some time throughout the week to also manage that, but as I said, this… this is just like a… From all the blog posts that we have, this is, let's say, an important one.
Yeah.
There was another blog post around the certification.
I think, like it was from a former colleague of mine at Cisco who took the OpenTelemetry certification and now offered a blog post about, like.
doing it.
I think… Atris, I don't know if you know, Dan, like, if it's okay to write this kind of blog post around a certification in our community blog, or if this is something like we have to share with, like, CNCF and say, like, hey, there's someone… I scan through it, and it's not like, hey, here's a set of questions they're going to ask you, and here's a set of answers. But I was just wondering if this is something we want to have on our blog, or…
**Patrice CNCF** 10:06 Is this the one that has the title, How to Survive Certification, or whether it's right for you? Is that the one?
**Severin Neumann** 10:14 Let me see how it is called… Is the OTC exam right for you? Yeah.
That's the one.
**Patrice CNCF** 10:39 I will… Take a look.
**Severin Neumann** 10:42 Yeah, I said, more like, hey, is this fine from a CNCF perspective, right? Because, like, I mean, technically the certification is owned by… by the CNCF, and not that someone says, like, oh, there's something we… you should have not written, and then… and yeah, that's the only thing.
I wanted to… Verify. Yeah.
**Patrice CNCF** 11:09 for… Bringing it to my attention.
**Severin Neumann** 11:12 Yeah. The other ones that is by TC… Needs some work.
The other one here is, there will be some other blog posts for that one, and then I talked with the OBI maintainers, they wanted to… make a 0.0 release before KubeCon with this.
Announcement, so it's, like, another one that Probably, if they can get the draft done soon, maybe also will come out.
Soon, yeah.
Any questions on the blog posts?
**Patrice CNCF** 11:57 While we're on this topic, I just want to mention, and you may have noticed, I'm less able to support, Coms, in terms of content?
I've been essentially focusing on infrastructure, so if there's anything Like you have done now, that you do want me.
To pay attention to, then tag me.
**Severin Neumann** 12:23 Yeah.
**Patrice CNCF** 12:23 I'll usually…
**Severin Neumann** 12:25 Yeah, no, I think… I think that's an important point that you call out, again, and this is always the thing around KubeCon, especially KubeCon North America. We're flooded with blog posts, And… and it makes me rethink how… how we… how we want to handle blog posts, right? Because… especially the last few weeks, especially for Tiffany, I think they took away a lot of bandwidth.
The good news is, like, we had a lot of community blog posts, right? We had a lot of SIGs… writing blog posts, which are the ones that we want, right? And less about those we also want the other ones, right? We also want the ones where people say, like, hey, I use OpenTelemetry, and here's something you can do with it.
But, like, we need much more of those blog posts where Sigs, they're like, oh, we released something, or, oh, we created something, or this thing is stable now, something like that.
That's really good, but at the same time, this is taking away a lot of bandwidth, so I think we need to be a little bit more… consistent on saying, like, hey, if the collector SIG is pushing out a blog post, then we also expect the collector's SIG to do some of the review work, right? Especially on the technical end of the things.
And we are more, like, doing the copy editing, and then saying, like, okay, this makes sense, let's shoot it out, right?
Yeah.
**Patrice CNCF** 13:52 Agreed. I assume that that's the case already. I'd hope so.
**Severin Neumann** 13:57 Yeah, yeah, it's more like, that we… I have the tendency to sometimes maybe forget about it, and then, like, have to… refocus on that, since it is just what I call it, because it happened to myself, right? I read the unrolled blog post, I reviewed it.
And then I asked the collector maintainers or approvers to take a look, and actually, I should have done it the other way around, right? I should have tagged them and said, like, hey.
Yeah, we need to be a little bit more serious about this sponsorship again.
To… to save ourselves time, right?
**Patrice CNCF** 14:30 Yes.
**Severin Neumann** 14:30 Yes.
Let me maybe put this here once again.
**Patrice CNCF** 14:36 Document that in our… Operations Manual.
**Severin Neumann** 14:41 B… Yeah, because, at the end of the day, at least I recognize that, like, I spent not a lot of time right now on docs, especially on writing docs, right? I would love to find time to write any docs, or review any existing docs and make them better, but, like, the whole… Review overhead is currently getting out of hand, and the blocks are not contributing to that, so… yeah.
So that's definitely one measure we should always keep an eye on to say, like, hey, blocks are awesome.
But this is not something we… we should… We should override our responsibilities around docs every time, like, we have this flood of blog posts.
There is a certain time right now with the GC election, and then with a few other things, like, a really, really high priority, right, where we say, like, hey, this is, like, house of the project.
But… but anything else, I think we can… we can slow down and say, like, hey, doesn't it make a difference if a certain blog post about someone using OpenTelemetry in a certain way, comes out this week or in two weeks from now, right? So, yeah.
It's just the call to action.
Yeah.
I thought we could quickly check about this issue once again.
Because, Patrice Vitor, I think you also looked into this a little bit.
I'm honestly surprised about that, because I thought that, like, by not using the GitHub token.
And by using, like, a bot token.
Like, it should be possible to re-trigger actions.
But it looks like we are back to that situation that, like, if we run a fixed command.
it's not executing the DCI actions, right?
**Patrice CNCF** 16:57 We… I think we're not… not using the GitHub token, so as you mentioned that, I'm think… so we… that… there may be mixed use.
**Severin Neumann** 17:07 Okay.
**Patrice CNCF** 17:08 in some of the scripts, so now that you mentioned that out loud, I'm thinking, Could… could that be… a contributing.
**Severin Neumann** 17:16 Let's see… Because at the end, what… What should… Go ahead.
trigger the… What should trigger the rerun?
is… Somewhere here, right? It's this part here.
**Patrice CNCF** 17:39 So, see… GH.
**Severin Neumann** 17:43 The actual thought.
**Patrice CNCF** 17:46 The right… it uses the right token.
**Severin Neumann** 17:50 Because it pushes…
**Vitor Vasconcellos** 17:51 Oop, yeah.
No, we are passing the token in all of the actions, but there's a checkout action earlier in this file.
That does not… has the… doesn't have the… the token, so…
**Patrice CNCF** 18:06 Right, you had mentioned that.
I think our conclusion was, let's give it a try, right?
And roll it back if… if…
**Severin Neumann** 18:17 Yeah, that's my overall… a comment on, like, testing those GitHub Actions did… Especially the moment you have a situation like that, that is really hard to test in your own repository.
The best thing we can do is just… tested on the live repository, right? So ideally, you have… you have one maintainer doing the patches, and one maintainer doing the reviews, and then going back and forth a little bit.
Since it's broken already, I'm not that hesitant to… To, to, to take a look into that, yeah.
**MG Marylia Gutierrez** 18:51 I was just checking, I was like, I think I did one, like… so yesterday I did one fix, and that worked.
**Severin Neumann** 18:58 Okay. Do you, do you remember…
**MG Marylia Gutierrez** 19:01 I'm sharing here the… on the chat, the… It was… the ref cache one, so… Yeah, if you scroll down, you're gonna see I have the comments, and then right after, the results.
**Severin Neumann** 19:17 But did you do the merged brain?
main… like…
**Patrice CNCF** 19:27 So, doing a merge will re-trigger.
**Severin Neumann** 19:32 Yeah. The actions.
**Patrice CNCF** 19:34 So what we're talking about is that after the bot submits.
**MG Marylia Gutierrez** 19:39 they commit.
**Patrice CNCF** 19:40 then…
**Severin Neumann** 19:41 At this point here, right?
**MG Marylia Gutierrez** 19:44 Okay, yeah, I don't remember that.
**Patrice CNCF** 19:45 - And usually that's my trick, is… I… If there's another PR that's been merged, then already we have that opportunity to rebase.
And I'll usually do a rebase. Otherwise, I look for a really trivial PR that I can approve and merge right away.
**MG Marylia Gutierrez** 20:05 Yeah, just keep a few, like, on the backlog and never merge, so we can use them. There you go.
**Patrice CNCF** 20:11 Little typo.
Hyphos.
**Severin Neumann** 20:16 Yeah, but it should work, right? I mean, it's like, here the… But yeah, maybe…
**Patrice CNCF** 20:22 going on, but, what Vitor said… Bye.
Rings a bell.
But I… I think I faced this issue with another workflow.
That the commit, the… sorry, the checkout also had to be… With the proper tokens.
Yeah, that could be right. That's what you're suggesting, right, Vitor?
**Vitor Vasconcellos** 20:48 Sorry, I… sorry, I was… I was reading your message here.
**Patrice CNCF** 20:52 No problem. You're suggesting we add the token for the… Checkout, as well.
**Vitor Vasconcellos** 21:00 Yes, yes.
**Patrice CNCF** 21:02 Okay. I'm not sure if that might be the…
**Vitor Vasconcellos** 21:05 I actually had this other discussion that caught my attention. It's a very similar problem.
Let me see if I can…
**Severin Neumann** 21:12 So let's do it.
**Vitor Vasconcellos** 21:13 instance.
**Severin Neumann** 21:14 Yeah, I think that could be the case, because, like, normally what Git does, or GitHub, I don't know who is doing it exactly in that case, but, like, the moment you do the checkout, it, like, writes the credentials it uses.
To poll, and then uses them for the push again, if you're not, like.
specifically take… I remember also seeing something like that in the past, so maybe that's helpful, yeah, let's… let's… It's… but then let's also comment… put a comment on the, like… like, when you create the pull request, write a comment, and like, hey, this is necessary. Because the checkout technically does not need the token, and we try to avoid not using the token whenever We've run an action that doesn't need it to avoid some security issues that we had in the past, right?
But if it's necessary, then let's comment on that and make clear, like, hey, this is also later used for the push.
Yeah.
Awesome.
**Patrice CNCF** 22:16 I think… I think I'm remembering the context is that I had not done a checkout in a workflow, and I was just doing… say, adding a comment to a PR, And it wouldn't allow me. The GH command would not work. I needed to check out the repo, even though I wasn't using the repo. So there seems to be some credential issues,
**Severin Neumann** 22:37 Yeah.
**Patrice CNCF** 22:38 business.
**Severin Neumann** 22:38 Yeah.
**Patrice CNCF** 22:39 on, as you mentioned.
**Severin Neumann** 22:40 Yeah, that's unfortunately a little bit opaque.
how this really works. But anyways, if this is fixing the problem.
We are done, right? So, yeah.
Oh, yeah, then let's… Meet, Awesome.
Next topic. More like… I mean, Vitorilia, you attended that meeting last week as well. Jay is doing this… Explorer project, right? Which is kind of… I… I call it Registry 2.0.
But let's see what it turns out to be. We met last week, and, like, had a few discussions on that.
from my point of view, I think… we are going, like, to look at a few different pieces here. The one is, like, the definition of metadata, and that's more something where we said, like, hey, this is part of the SIGS themselves, right? Because Collector has been doing that already. Java has a little bit of that, a few SIGs have that already.
than the collection of the metadata, this is more like… just things that Jay… Is exploring right now, and we have a little bit of this in… in our repository as well, right? But it never… besides a few building blocks, it never turned out to be, like, a full solution, right? And it's a good question if this even should live.
In the comps repository.
And then the third part is, like, okay, when we have this data, how do we visualize it? How do we make it accessible, right?
And one part could be, like, the website and the registry. So I think right now we are… We're leaning towards saying, like, hey, maybe we need just a central place where, like, all this open telemetry metadata lives, and then people then can consume it and then pull it in whatever places they want to have it.
That's kind of just thinking right now.
**Patrice CNCF** 24:51 So, is this… specifically related to what Jay is working on, which, if I remember correctly, is just in the context of the collector.
Or is this broader in terms of, really, the registry 2.0?
**Severin Neumann** 25:07 No, it's instrumentation libraries and collector components, which is kind of 80% of what the registry is doing, right?
**Patrice CNCF** 25:14 Okay.
**MG Marylia Gutierrez** 25:15 Yeah, but he didn't even start with the collector, he pretty much started with Java.
Nice to my question. Yeah.
**Patrice CNCF** 25:22 Okay, right. Yes. Okay.
**Severin Neumann** 25:24 I think… I think, like, like, what he started with is the Java part, and there he also took care of the definition of the metadata and how they want to do it, right, in their repository. And then he wrote, like, the piece where he, like, represents this data, and I think he also, if you remember, he created this collector watcher, or whatever he called it.
That's, like, pulling in data, and then, like, trying to, like, have this listing of collector components, versus, like, yeah, this is, like.
A little bit of duplicating the work of the registry.
So yeah, but right now, I think the… So, in my ideal version of this, it's like… gradually phasing out what we have in the registry, and I don't know if it's then going to be a dedicated app you're linking to, or if it's still part of the website. I think those things that need to be evolved, right? We need to see what works and does not work.
**Patrice CNCF** 26:22 So, is exploring this more in depth in the first quarter of next year?
More realistic, or you want something… or is he… You, we, looking for something before end of year.
**Severin Neumann** 26:37 I don't know, honestly, what, like, what, like, the timeline is here, right? So J seems to be… Spending a good portion of his time on that.
So yeah, I suspect that we make some progress already this year.
I think right now it's also, like, the question, like, is this partial comms, or is this, like, going to turn into, like, a dedicated part of the project? I think there's, like, that's the project proposal.
in Community Repo.
So maybe I can link this back, and then we can, like, also talk about this a little bit more.
Yeah, but if you have any considerations or any concerns, I think that's also something. We also have created, like, an inofficial Slack channel for that, so there's, I think, how is it called?
Hotel Ecosystem Explorer.
Or something like that, to just coordinate that a little bit.
So yeah, but a lot of those things are just, like, in flux.
So this is definitely also the time to… to bring in any… any questions or concerns.
**Patrice CNCF** 27:48 I am interested, since this is kind of infrastructure and kind of the area I work in. I don't know how much time I'll have between now and the end of the year, it's probably not much.
**Severin Neumann** 27:57 Yeah, yeah.
**Patrice CNCF** 27:58 I was saying that. But, If this is kind of a pilot project, And I can see how… how it pans out. If you're thinking, no, it's more than a pilot project, then I'll… I'll tr… see if I can carve out some time.
Take a cold.
**Severin Neumann** 28:17 I think, yeah, I think what would be good, if you can carve out a little bit of time, if you can, like.
just be in sync, and especially provide guidance, right, especially from a CNCF perspective, and say, like, hey.
does it make sense to… like, for example, there were a few discussions also around, like, how does this relate to things like backstage or artifact… artifact up… what a difficult word.
I mean, there's some kinds of that in CNCF already, right? So is it a big question?
**Patrice CNCF** 28:51 leaf.
**Severin Neumann** 28:52 How do we align with that, right? And that's also why I think that, like, separating out The definition, the collection of the metadata, and the presentation of the metadata makes a lot of sense.
Because depending on how this plays out.
Maybe we're also feeding into some of those resources, right, that we say, like, hey, maybe there's a way to feed maybe let's start with collector components and feed them into the artifact app, right? Or maybe people say, like, oh, we run Backstage, and we want to leverage some of that information.
So, so that by decoupling a little bit of, like.
how the data, like, like, having some kind of open telemetry data lake, I think that's how I called it last week.
would help us to, like, feed this into different sources, right? And then make sure that, like, oh, different… People can make sense out of this data.
That's why I said, like, yeah, let's not… Have, like, this… ecosystem Explorer and the data, like, as one dedicated component. Let's think also about, like, making this data open data, so to speak. So, but yeah, that's very nascent, so let's figure this out over the next few weeks and months.
**Patrice CNCF** 30:13 Okay. Yeah.
**Severin Neumann** 30:15 Cool. Thank you.
I thought I'd bring another topic to the agenda, because, like, Pablo opened this up a few weeks back, and I think we have not really… Talked about this in detail.
So, so the idea was, like.
So maybe I need to step back a little bit to explain, like.
where this is coming from. So I think this was also a cheesy discussion, where we said, like, hey.
how… How can we make it easier, especially for existing contributors, and especially for maintainers.
To distinguish noise and signal around announcements within the community, like… I don't know.
We are launching a new project, or here's a new process how we do certain things, etc, etc, right?
Right now, we tell people, of course, like, hey, attend the specs meeting, or look into the maintainer Slack channel, but, like, at the end of the day, it's like a multi-channel thing.
And it looks like other projects are doing the same thing. The question is, like, should we have those kinds of separations?
I think an easy way would be something like categories.
Right?
But yeah, that's just something… I think, Patrice, you might have some ideas on that as well.
**Patrice CNCF** 31:47 I… My suggestion to look for alternative solutions is because… so if you can open up a tab over the blog.
**Severin Neumann** 32:00 Or blog, you mean?
**Patrice CNCF** 32:02 our blog, you know, the hotel blog.
**Severin Neumann** 32:04 Yeah, just give me a sec… here's our block, yeah.
**Patrice CNCF** 32:12 So, so right now, on the left, the folders are… are per year.
Yeah. So, if you collapse that, then you see it's per year.
My initial reaction was I wanted to avoid having two categories here. One would be insider, and the other one would be… would be rest community, or I don't remember what we called it.
Hence the suggestion to use tags or categories in the blogs.
**Severin Neumann** 32:44 Yep.
**Patrice CNCF** 32:47 Or, we happen to create a separate blog stream that's accessible differently, just for insiders.
those are the options I can think of.
**Severin Neumann** 33:00 Yeah, yeah, I mean… what Cates is doing, right? I mean, they have to… they have, like, their secondary domain, right? They have… I.O. blog, and they have their dev blog, but it's, like, a completely separate From my understanding, this is like running in a completely separate instance, I'm not very happy about that idea.
Like, like, this is, like, their getting started documentation for the whole, like, open,
**Patrice CNCF** 33:29 Right. Tates ProCheck.
**Severin Neumann** 33:31 I'm not really sure if this is, like, the thing that we should be doing.
**Patrice CNCF** 33:35 No, I agree. I think…
**Severin Neumann** 33:38 Yeah.
If we… if we could do tagging, and maybe… so my understanding is also, like, people, for example, also rely on on, on RSS feeds, or if they can do something like block slash and then maybe also apply a filter here.
Even if it's not linked from the website that easily, right? Or if it's, like, for example, you go into community, and then you have your announcements, and then it goes back to blog, and that kind of filter. I think… at the end, I prefer easy over perfect, right?
How difficult would it be to roll out the categories? Is this, like, something…
**Patrice CNCF** 34:21 It's built into Doxy, so if you go to Doxy, open up a new tab and type doxy.dev.
Yeah.
There you go, so you see, click on one of the tags.
Or… or categories. But essentially, you get a list of, entries.
**Severin Neumann** 34:39 Okay, yeah.
**Patrice CNCF** 34:40 Now, I mean, these are just demo, they're not… Serious.
**Severin Neumann** 34:45 Yeah, yeah, there's just, like…
**Patrice CNCF** 34:47 But essentially, you get a list, so… It's built in, we could start using it now.
The interface may not be as friendly as just seeing a blog like this with entries.
The alternative is to have under Community an insider blog, and it could be completely separate, and that way we've got contributor, or, what did I call it? End user blog, which would be the main blog in OpenTelemetry, and then there would be a blog-like Insider section.
So that's an alternative to… to tag.
**Severin Neumann** 35:32 That we, like, have here in community, and then something like… And telemetry inside, or blog, just community blog, or something like that, and then… Yeah, okay.
**MG Marylia Gutierrez** 35:44 get us either option, will I have to go back to all?
Preview or publish posts to tag them correctly?
**Patrice CNCF** 35:54 If we go with the tagging solution… well, I guess, yes.
**MG Marylia Gutierrez** 35:57 Both ways, yeah.
**Patrice CNCF** 35:59 both ways. Either we tag, or we.
**MG Marylia Gutierrez** 36:03 Move things, okay.
**Patrice CNCF** 36:05 Or we could choose not to move.
To move them in whatever…
**Severin Neumann** 36:12 And only tag… only… only tag the new ones, or say, like, hey, we go back the last 6 months, or something like that, and only tag those, and the rest is just untagged, right?
Good advice.
**Patrice CNCF** 36:23 Especially since we have a one-year cutoff policy, so after 12 months, I don't know if you noticed, but blog entries that are older.
Have a disclaimer at the top.
Have you seen that?
**MG Marylia Gutierrez** 36:35 Yeah, I never noticed, yeah.
**Patrice CNCF** 36:37 Okay.
**MG Marylia Gutierrez** 36:38 Now I'm opening an old one now, because I'm curious.
**Patrice CNCF** 36:41 Yeah.
And so… Because our site is… Getty.
Hi.
**MG Marylia Gutierrez** 36:52 See enough, yeah.
**Patrice CNCF** 36:53 We are not doing… we don't do link checking, we don't do… there are a whole bunch of checks that we stopped doing for the old blogs.
Just because it became too much of an overhead to maintain.
**Severin Neumann** 37:05 Yeah.
**MG Marylia Gutierrez** 37:06 I imagine, yeah.
**Patrice CNCF** 37:08 So, in that.
**Severin Neumann** 37:08 Okay, but…
**Patrice CNCF** 37:09 We probably would not go so far to tag all of them, but we might tag within the past 12 months, or reload. I don't know if we want to relocate.
Yeah, I guess… I don't know what… if we want to vote here, what the general feeling is. Kind of feel like tags might be better, so whatever insider posts would be, we'd have an insider tag, and then…
**Severin Neumann** 37:33 Yeah, I would… I would… I think I would prefer tagging, and then maybe find a way to… Let people in the community know, like, hey, here's a way how you can only see those blogs, or we find a way to… to send them to them In a… In a convenient way.
The other day, like, like, semi-related to that, right, I mean, there is the… I'm not sure if you're aware of that, let me see if I can find it.
There is the… Cncf, mailing lists.
Ryan?
Listcncf.io.
And there is an announced list.
Just stopped sharing my screen, I'm not sure how much of that data is… publicly available. But there's, like, a… There's, like, a mailing list, there's, like, a mailing list called cncf-opentelemetry-announce.
And I think it has around, like, a thousand-something reader.
But we never published anything to it, so I'm wondering, like, how hard it would be To… to feed it from the block, right?
**Patrice CNCF** 38:52 Oh, I thought you were going to suggest that as an alternative. I was going to say, yes, we don't have to make any changes to the website. Just post to there.
But.
**Severin Neumann** 39:06 No, I mean, the question is then, like, if we have the tags, we could still say, like, we send everything to announce, and then there's maybe the contributor channel, and we feed into that, and yeah, back to CI and automation.
Oh, we love it. I mean, I could… I could also subscribe to do it… to do it, manually, or we can also subscribe, especially for the community ones, that we say, like, hey, the moment we have one, we push it out to hotel maintainers and whatever.
yeah.
**Patrice CNCF** 39:35 Okay.
What's the relative priority of this?
So the tags are there, but I'm seeing, a mention of RSS feeds, I… don't know if there are SS feeds for the… For that tags page. I also don't… I've not seen any project that uses it extensively, so I don't know what the user experience is.
That much.
So I do want to give that as a disclaimer.
**Severin Neumann** 40:12 Yeah, yeah.
**Patrice CNCF** 40:12 So, coming back to the question, juggling priorities, as we… Work through this last quarter.
**Severin Neumann** 40:22 I, I think… If… if turning on tags is, like, easy.
Right? If we say, like, we can't just turn it on and… Give people at least a starting point.
**Patrice CNCF** 40:44 So, feature in terms of separate lists, that's that the tags… And or categories will provide that.
RSS feed, I'm not sure.
And.
**Severin Neumann** 41:03 My problem with that, like, I'm not a big fan of, like, not showing the community stuff.
Right. So, I'm not a fan of that.
**Patrice CNCF** 41:14 I was gonna… that… I was coming to that comment as well, how much… Is our community actually wanting such a feature, or needing such a feature?
**Severin Neumann** 41:25 At this point.
**Patrice CNCF** 41:28 One blog stream, it's clear.
**Severin Neumann** 41:31 I think it's more like, for me, and maybe we need to follow up with Pablo on that.
But for me, it's more about, like, hey, I, as a maintainer, approver, contributor.
need to know if there's something I should pay attention to, right? Because it's like an announcement. Think about GC elections, think about TC elections and nominations, right? I think that's important to To most people that are contributing to the project, right?
Versus, like, hey, here's a new cool thing that the collector is doing, right? So… Yeah, that's more important to me than, like.
showing not community content to not community members. I mean, we want everybody to join the community, so we should not… We should not do that.
But yeah, maybe let's get back to the issue and, like, if… but priority-wise, if it's easy to add tax and categories, then let's roll it out and see what we can get out of the box. But if you say, like, hey, this is a bunch of work, and, like, breaking things, then I would not say this is a priority right now compared to other things.
**Patrice CNCF** 42:48 Okay.
The feature's there already, all we need to do is tag blog posts, and the tags will appear, I believe.
**Severin Neumann** 42:58 Okay.
**Patrice CNCF** 42:59 No, that's not true, there's a bit of config. Okay, I'll… I'll work on it.
**Severin Neumann** 43:04 Yeah, but as I said, if it's more like a few hours, and especially a lot of headache, then let's not do it. But if you say, like, hey, this is something I can do in half a day, then… I think it's… it's worthwhile.
**Patrice CNCF** 43:17 And I can't promise RSS feeds, but I will.
**Severin Neumann** 43:20 Yeah.
Yeah, I also don't think that's the most important thing.
Okay.
Yeah, let's ignore that one.
And then… Cool. Training and ops? Who has added that? I have not added that, but…
**Patrice CNCF** 43:38 I added that. I just wanted to reiterate that one of my… Objectives and hopes before the end of the year is… Already proposed, operations manual, which is now in Google Docs.
I think a few of us are… I know Vital has, and Febby, have been playing around with Copilot and other AI agents.
So, to me, that's… A motivation, because our doc… our operations documents become executable.
I think our documents in general become executable, and that gives much more value to, Extra value to our… to the documentation efforts.
So, I haven't had time yet, but I do want to push out Something to the website that… We'll encode our… operations and procedures.
In the meantime, I'm updating the Google Doc.
**Severin Neumann** 44:46 And… Okay.
**Patrice CNCF** 44:48 Vitor has used one section, I believe, so far in… Successfully.
I added that bullet because I was gonna propose, a shadow session, for Vittor, but wanted to see if… is it, Marilia?
Is that pronounced correct? Am I pronouncing it correct?
**MG Marylia Gutierrez** 45:13 You can say both, like, Marilla or Morelia, yeah, let's it.
**Patrice CNCF** 45:17 Okay.
**MG Marylia Gutierrez** 45:18 Like, how we say, like, in Brazil it's Mariglia, but for English.
**Patrice CNCF** 45:23 Yeah, man.
**MG Marylia Gutierrez** 45:23 Versus.
**Patrice CNCF** 45:24 So I… okay.
**MG Marylia Gutierrez** 45:25 I kind of created Morelia, that works as well. Morelia, okay.
**Patrice CNCF** 45:29 I…
**Vitor Vasconcellos** 45:30 For me, you can say Victor, too. It's… it's the same, I'm…
**Patrice CNCF** 45:34 Okay.
**MG Marylia Gutierrez** 45:35 I think V…
**Patrice CNCF** 45:37 Vitor, like…
**Vitor Vasconcellos** 45:38 like.
**Patrice CNCF** 45:38 Cooler.
**Vitor Vasconcellos** 45:39 Great, thank you. Yeah, for me, when he…
**MG Marylia Gutierrez** 45:43 Yeah, when people started saying, like, I already, like, replied because I know it's me.
**Patrice CNCF** 45:49 Marina. I… so, yeah.
I practiced Portuguese for… two terms.
was interesting.
It's fun.
So, marilia. I wanted to know if you were interested in joining the sessions, So what I would cover, firsthand, and, and I know Severin, you've been doing them, so I don't know, we keep them separate, we combine them, we… it might be too much to combine, but, to have a session to look at Ref cache updates?
And what to do with that, and build up some expertise there. And the specification integration, which is important.
and requires quite a bit of expertise. So, do you think you'd like to join those? Should we schedule them together? Or should I… how… how would you like to be involved in those two activities? And feel free, like, we have that document assignment… assignment of areas page, so feel free to… to say no if your hands are full.
But you're welcome to join.
**MG Marylia Gutierrez** 47:05 Yeah, I can join, like, I don't wanna, like, to be the one… saying, like, let's do this day or that day, just because in case I cannot join. I don't want to, like… I can adjust, like, my calendar and show up, pretty much, yeah.
**Patrice CNCF** 47:18 Okay.
**Severin Neumann** 47:20 I mean, I have scheduled one shadowing this week. I can also, like, Patrice, if you do something this week, I can… I think, Marilia, you also suggested that Tiffany's doing that at some point, because, like, you're at the same company, and, like, time zone-wise, it's better. So… for me, the important part about shadowing and, like, having those one-off meetings is more, like, to make it easier for you to get started, but whoever does this, and if it's… I think it's even better if we, like, mix it from time to time, because, like, everybody of us has different expertise.
So yeah, I think maybe… maybe we can even put this also in our ops doc, but maybe the idea is, like.
existing maintainers should offer that, and, like, send out an invite to everybody, and people can join whenever they like, right? I mean, even if, like.
Patrice, if you do anything, I'm, or maybe also Fabradi or Tiffany, sometimes interested to… to hear and see how you do it, right? So, maybe let's keep it as an open forum, focused on, like, the new joiners that you say, like, hey.
Find a time that works for you.
And whoever is new right now, right? And maybe other people in the future, and that way we can maybe establish that as a good practice. I think that's… that's how I think about it.
I think we have scheduled something for tomorrow, or Thursday, or something like that, I can even cancel that, and… And, and, and you can… What… what time was it?
my 330.
Patrice, I sent you the invite, and if this time works for you, perfect, and if not, we can… Schedule something else, right?
Let me… That's good.
**Patrice CNCF** 49:04 I saw something go by, I don't… Remember.
**MG Marylia Gutierrez** 49:10 I have to double-check on your email.
Yeah, this one, I can see the invites is just for, well, me, Severin, and Vitor.
**Severin Neumann** 49:18 Yeah, exactly, so I will send it over to you as well, and… Maybe we can find a way to… Can we have, like, a distribution list on… on Google. Maybe I figure out a way that we have something where we call just the… all the maintainers and approvers and then send it out.
I figured something out. But I will send that one specifically to you, Patrice, and then you can see if this time works for you as well, and if not, find another time. It's just like, I think it's good to have some regular cadence on… on meeting outside of this This official meeting, where we also hope to have newcomers join us, so…
**Patrice CNCF** 49:59 Sounds good. So, have you already planned content for that meeting?
**Severin Neumann** 50:05 No, nothing. It was more like, let's put something in the calendar, and if… If there's any questions, we can go over that, but since you have specific content planned.
**Patrice CNCF** 50:14 Thank you.
-
**Severin Neumann** 50:16 I'm more… I'm more than happy to… to have you… to have you manage that, so, excellent.
Yeah, now I have to… time, info.
I sent it to you, I said, but if you think that's not…
**Patrice CNCF** 50:34 What time is it for you, retar?
**Vitor Vasconcellos** 50:38 It's 11.30.
**Patrice CNCF** 50:42 Oh yeah, okay, that makes sense. Then that'll… I just canceled another meeting, so that will work.
**Severin Neumann** 50:51 It's for half an hour, so… And right after that, again, I have this meeting with JSBIL, So, I can also… and mind.
some of you to that on the Instrumentation Explorer, if you want to join that as well. Once again.
That's right after that.
**Patrice CNCF** 51:09 Now your picture is bigger, Maridea. I can see this cool car collection you have.
**MG Marylia Gutierrez** 51:16 So, I'm actually on… Well, because I have the event from Grafana next week, so I'm currently in Brazil, and I'm at my parents' house, and this is his office, so he has a lot of cars. And next to me, there is more, and on the table, there is more. And where it used to be my bedroom, he just, like, dominated and put more cars there as well, so it's just, like.
**Patrice CNCF** 51:39 Tahoe.
**MG Marylia Gutierrez** 51:39 cars all over. Cars.
**Patrice CNCF** 51:44 Wow.
Impressive.
**Severin Neumann** 51:50 Awesome.
Yep.
Anything else? I think we have… Had a lot to go through, so, And yeah, I think we see each other on Thursday.
**Patrice CNCF** 52:04 Excellent.
**MG Marylia Gutierrez** 52:05 See you then. And then I will see… and I will see Vitor in person next week.
**Severin Neumann** 52:11 Awesome.
**Vitor Vasconcellos** 52:12 We're hosting… we're hosting something, like a talk in… at the office, so… I invited Marilia to join us, and we're gonna talk about open source, open telemetry, Cool.
**Severin Neumann** 52:29 Awesome.
**Vitor Vasconcellos** 52:30 So… I can share with you later, it will be in Portuguese, but I'm pretty sure…
**MG Marylia Gutierrez** 52:37 Your chance to learn… Yeah, YouTube will trans… yes!
**Severin Neumann** 52:44 Awesome.
**Vitor Vasconcellos** 52:45 So cute.
**Patrice CNCF** 52:46 Okay.
Thank you all.
**Vitor Vasconcellos** 52:51 Thank you. Bye. See you, Made too.
