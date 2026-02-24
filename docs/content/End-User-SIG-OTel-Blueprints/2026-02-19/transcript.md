SIG: End-User SIG: OTel Blueprints
Date: 2026-02-19
Duration: 225 minutes
Zoom Recording URL: https://zoom.us/rec/share/NCCX_kJw6szElzEBDkE_CzI2JvGHGma0cG0l-OgzhWFwLuwke2bDhthKegaLcLkX.b99pNzuD6gn6tYDM
============================================================

## Zoom Recording Transcript

lciukaj@splunk.com 03:16:48 Hey, Joey.
Can you hear me?
Hello?
Are you there, Joey? Do I pronounce your name correctly? It's Joey.
neil yashinsky 03:22:19 Hello all. Oh boy, did we get another AI note-taker again?
lciukaj@splunk.com 03:22:24 I know. Hey, how are you?
neil yashinsky 03:22:26 Good, and yourself?
lciukaj@splunk.com 03:22:27 I'm good, thank you for asking. I was just wondering if someone else joins today, because I know Dan and Tiffany, they are…
I mean, Dan is in PTO, but she cannot join, so she even suggested to cancel this meeting, but then that time I volunteered to be a lead, so…
So I decided to join anyway, and maybe wait a few more minutes. We have Joy as well on the call, but Joy is not responding. I don't know if he…
So…
neil yashinsky 03:22:59 Oh, go ahead, please.
lciukaj@splunk.com 03:23:00 Yeah, agenda for today, I think it's…
it's… it's simple, so we need to review the board. I don't know if there is, like, lots of progress.
I wanted to start working on my blueprint for non-Kubernetes environments.
But then I remember… And Dan suggested to first, make sure that we have Our, template finalized.
neil yashinsky 03:23:25 Yeah.
lciukaj@splunk.com 03:23:26 So I think that's our main focus now.
neil yashinsky 03:23:30 Makes sense. Yeah, I was trying to figure that out, too, when I looked at the board last time, and there's… because there's, like, you know, obviously classic dependencies or whatnot, so.
lciukaj@splunk.com 03:23:39 Right.
neil yashinsky 03:23:41 I looked, and I think in some ways, like, Alex was doing a good job of leading the way, but I wonder if there was, like, one other update that I made that maybe didn't make his, or he didn't like it, I wasn't positive, I didn't want to assume.
lciukaj@splunk.com 03:23:54 Yes.
neil yashinsky 03:23:55 I just kind of waited, because he, you know, he did a great job the first, took the first stab at things, and then I tried to address some of the feedback from the other parts of the thread. I think it was in 35.
lciukaj@splunk.com 03:24:09 Which one would… for… 2.35, or… Yeah, let me double check, because there was some of it in both.
Oh, no, it is 247, sorry, it is 247. Yeah.
neil yashinsky 03:24:21 If you go to the very bottom.
lciukaj@splunk.com 03:24:22 I think there should be some link, right?
neil yashinsky 03:24:26 Yeah, there is, there is.
lciukaj@splunk.com 03:24:27 Exactly.
neil yashinsky 03:24:28 Exactly. It's your blueprint.
And I wasn't sure, like, it's, it's good, but, like, I did provide feedback on the format, if you go back to the thread.
Above that, there's, like, two… yeah, so the first, if you go above it a little bit more, just a little bit more, like, my first, my first, yeah, that one is, like.
acknowledging the work that he did, because I think it's got things started, and then, like, this is the format that I kind of suggested based on, I forgot her name, but, you know, earlier she talked about how, like,
You know, including the, the challenge, you know.
lciukaj@splunk.com 03:25:13 Who are the…
neil yashinsky 03:25:14 proposed structure of challenge, benefit, actions. And so I tried to reformat what he had, or maybe extend what he had for that, and then he took what he had and turned it into the document that we should have. Yeah, so I, like, merged what he had and what I had here, and then when he created the document that he did, which was good.
Because it was mentioned, like, none of my feedback made it back, I don't think, or was rejected.
lciukaj@splunk.com 03:25:39 absurd.
neil yashinsky 03:25:40 So I didn't want to assume what happened, because there's good stuff in there, and I, you know, so I'm certainly too new to be, you know, raising, I mean, I just wanted to, like, highlight where… what the diff was, you know, and, and…
How, if at all, they had been merged, or they may have just been, like, if you will, they're separate branches of work.
lciukaj@splunk.com 03:26:03 That's right. You know, so I'm a bit confused as well. It's a picky with anyone working on that blueprint, because, yeah, I see there is, like, lots of good comments from you here, like, about the structure, and how this should be updated, which I agree, right? I look into the Google Doc, it's not yet, like, included, right? So I think it's not…
neil yashinsky 03:26:26 Right. So there is.
lciukaj@splunk.com 03:26:27 There's still some work that needs to be done here.
neil yashinsky 03:26:30 Right.
lciukaj@splunk.com 03:26:31 So it's more about… yeah, this is more about the scope, so it's not yet the actual content, that's my understanding.
neil yashinsky 03:26:38 Yeah, I think, like I said, I think it was kind of like, this was, to further the work that he did along that line, and it makes a lot of sense. But yeah, I think to your point, like, it's more metadata than data, if you will.
lciukaj@splunk.com 03:26:51 Correct.
neil yashinsky 03:26:51 at this point.
lciukaj@splunk.com 03:26:54 From my perspective, I'm not sure… I think that's something we need to discuss next time, like, what we are, like, missing in the current blueprint template, why we are not yet ready to accept it and agree together that this is a good template.
neil yashinsky 03:27:09 I think it was. I think it was moved from… forgive me for interrupting, but I think the last time we did that, if you look at 236, I think, that's what.
lciukaj@splunk.com 03:27:21 2, 3, 6, draft reference architecture template.
neil yashinsky 03:27:23 Dan did in 236, I think. But it may… it may… it may have been, like, yeah, I think at the very end, he's like.
he created the PR, right? So I think… I think once we, I guess, merge that PR or whatever, then, like, we're done with, like, at least the draft, and maybe we'll refine it later.
So I… but again, I'm like… so new to the Blueprint project, I didn't… I, you know, and I don't even think I had access to the board if I thought it was what I should do, but I failed a lot.
lciukaj@splunk.com 03:27:56 Yeah, but here's the… here's the PR that Dan opened. Here's the PR that Dan opened.
neil yashinsky 03:28:02 Oh, I see, I see.
lciukaj@splunk.com 03:28:03 Yeah, so this was, like, opened 2 weeks ago, and there, if I go to Files, and go to the…
So this is… this is exactly the blueprint. So, the template. So I'm just wondering if this is the final… I mean, to me, it looks good. I mean, I can follow that, and I can start working on the one that I wanted to lead.
So…
Frankly speaking… and yeah, so even if there will be some changes to the structure, we can always update our…
neil yashinsky 03:28:32 3.
lciukaj@splunk.com 03:28:33 So there is no, like, you know, that we need to start from scratch, it's just, you know, updating the paragraphs, etc. So… so I think that if there are…
the teams that want to continue working on some blueprints, they should start working, it's not… I agree.
no need to wait on the… on the final. I know from the project management perspective, it makes sense to have everything prepared, ready, finalized, but… but again, just to note… because… so from my perspective, I could start, like, like a week ago, but when I was waiting on the… on the…
neil yashinsky 03:29:05 if on the.
lciukaj@splunk.com 03:29:06 a template to be ready? Yes.
neil yashinsky 03:29:07 Yes, exactly.
lciukaj@splunk.com 03:29:09 I'm gonna start working on that, so I will start… this is 245, non-K, non-Kubernetes environments.
So I'm gonna put the Google Doc, and again, start putting some text there. We'll figure out later the template and the sections, so there's nothing we should wait on. That's my understanding.
neil yashinsky 03:29:33 I agree.
lciukaj@splunk.com 03:29:34 And I remember from the previous, call that we had, where is… this is the end-seq end user, this is the last blueprint? Yeah, that's 2 weeks ago. So I remember we were discussing about which blueprints we should focus on first, right? So that is something…
I believe it's still not… Not finalized.
And I didn't see any discussion about that in any other thread, because currently, if we look into the board, we have, I believe, 3. Blueprints for…
instrumenting infrastructure and processes on non-Kubernetes environments, that's something where I would like to contribute. There is also looking for centralized telemetry platforms, so that is something what Dan was suggesting since the very beginning about where to put the collector for this, like… Interesting.
neil yashinsky 03:30:21 Yeah. Enterprise.
lciukaj@splunk.com 03:30:22 enterprise environments, and there is the last one, which I believe you are part of, Neil, right? The Kubernetes Observability.
neil yashinsky 03:30:29 Yeah.
lciukaj@splunk.com 03:30:30 Yeah, so we have 3 now, which is good, good start, but I'm not sure, maybe we need to discuss others, or just finalize this free habits.
neil yashinsky 03:30:41 Yeah, there was a bit of a discussion, I think. I feel like, on the last call, it may have just been in the chat, actually, but if we looked at the… or two calls ago, even, there was, discussion. I think you're largely correct that, the 3's a good… or the 4, because I think you mentioned there's one on there that you want to contribute.
If I heard you right. And then, yeah, I think there was just, like, one other one that Alex, I thought, had mentioned, basically, like, I think there was a variation of, like, VM, you know, virtualized-esque, non-Kubernetes, like, old school, I want to call it, or whatever, you know.
fee-sphere-y type stuff, or whatever. That's not really my bag, per se, but,
But yeah, I think… I think there's obviously, mainframe-type stuff, too. Not saying that should be on our… on our, you know, to-do list right away, but I think, like, if we're trying to reflect the community or whatever, then that's an important…
use case or whatever that's worth covering, but again, who's assigning that, who's going to be doing that, or whatever? My point was just, like, I feel like the domain is… is… like, we have identified a few, but it's still open to your, you know, kind of, to your point that, like, there's stuff that's missing that we should
People should feel free to start working on, if they have the insights and, you know, intuition to lead on it.
lciukaj@splunk.com 03:32:07 Exactly, I will put a comment here that even though the, blueprint…
blueprint template is not yet finalized. Teams… Might start working on…
individual groupings. So that's my understanding. That's what I'm gonna do.
As well, and so this is the template for the board itself,
I think we should put some comment, like,
Whether… should we keep the free… Should we… Keep… pre-existing blueprints.
neil yashinsky 03:32:51 Or just how many blueprints, you know? Yeah.
lciukaj@splunk.com 03:32:54 Should we include, other ones?
neil yashinsky 03:32:59 Yeah, scope. Blueprint scope, I guess.
lciukaj@splunk.com 03:33:01 Yeah.
Something like that, so…
neil yashinsky 03:33:05 Sounds good.
Sounds correct.
lciukaj@splunk.com 03:33:07 So this is the one, but when it comes to the others, when I look into the board, I don't see any progress. For centralized telemetry platform, what we got here? No, this is just…
just something what Dan started, and no progress here. And the one that I'm leading, again, no progress here. I put a comment here, we have, some…
other contributors who want to contribute to that, Gabrielle and someone else, I don't know what name exactly here, but we have at least 3 people who want to work on that, so again, I'm planning to put
Google Doc for this, and start putting some content, getting other contributors to this one. And the last, which we have on the list about Blueprint for Kubernetes Observability. Yeah.
couple of folks here, and you, Neil, as well, who are part of this mini-team, so… and Docs is already here, so I think, from my perspective, we can start working on this, to… Yeah.
Move forward with this.
Cool. So, other than that, I don't see anything on the… okay, agree on tool and style for the blueprint diagrams. I believe there was.
neil yashinsky 03:34:25 Right.
lciukaj@splunk.com 03:34:26 about that, right? What tools should we use?
neil yashinsky 03:34:29 Yeah…
lciukaj@splunk.com 03:34:30 There will be some graphics that might be later updated, so we need to make sure that this is easily being updated.
neil yashinsky 03:34:37 Correct.
lciukaj@splunk.com 03:34:38 which can be updated, so I believe someone suggested Mermaid here last time.
neil yashinsky 03:34:44 Yeah, that's already being used, and I forgot there was, like, one or two instances where Mermaid was not applicable that, was… it was suggested that we might need something, outside of… outside of Mermaid. I forgot.
lciukaj@splunk.com 03:34:58 It's D2, declarative diagramming. I don't have any problems with this, but I need to double-check what it is and how it works.
neil yashinsky 03:35:06 I meant specifically, like, the use case that Mermaid was, like, it wasn't well-suited for, and D2 was. Yeah. Because I just played around with it a little bit, and it seemed good to me, when I… when I tested it out. But I'm not an expert, you know, so…
lciukaj@splunk.com 03:35:21 Is it more like you need to describe what you want to have on a diagram, and this is then created magically, this kind of style?
neil yashinsky 03:35:28 I mean, I think I basically… it was kind of like you generated it from the, you know, the source…
I think itself was, like, basically it was, you know,
what's the word I'm looking for? You know, it generated the graphics, the modeling, the images, based on dependency diagrams, you know, or dependency…
requirements built into the repository itself, I believe.
So, it was a little while that I did… I did… I put my comment two days ago, but I did my experiment several days ago, so I don't remember all the details. But yes, I think it was basically, like… I mean, I think there's lots of ways you can use it, but I think your… the way you described was included in that.
lciukaj@splunk.com 03:36:14 Yep.
So I think that it's gonna be, Google Doc… why it's… Should be new list.
It's weird.
neil yashinsky 03:36:28 Yeah, like, the list, it's like, somewhere in there, it's like, yeah, yeah, there you go.
lciukaj@splunk.com 03:36:34 It's really good.
And here we should, put, like… G.
neil yashinsky 03:36:41 Yep.
lciukaj@splunk.com 03:36:42 So, Google Docs… or collaborating.
neil yashinsky 03:36:47 Yeah.
lciukaj@splunk.com 03:36:47 One of the blueprints.
This is, like, before the PR, right?
then if we have it… we discussed that before, right? That we want to have blueprints being part of OpenTelemetry.io, so once we have the section created there, we'll be opening PRs, we'll be moving content there, but… Right.
neil yashinsky 03:37:10 I'd almost say for drafting even, collaboratively. I don't mean to, like, word police you or whatever, but I think that's, like, your essence of what your point is, yeah.
lciukaj@splunk.com 03:37:21 Before PA open elementary.
be honest.
And then we have… how was that? Detour, right? Yeah.
D2.
neil yashinsky 03:37:32 If you go to the very top of that thread, I think it has a good, like, explicitly…
What it was… for, like…
Specifically for the diagrams, I think. Yeah. Yeah, yeah, yeah.
So you didn't have to reinvent that wheel.
lciukaj@splunk.com 03:37:49 This is the virus. Okay, so, okay, so this is something like this, right? Yeah, yeah.
Define, and then you get a diagram. Yep, that makes sense.
And then it's obviously easy to update it later as part.
neil yashinsky 03:38:06 Right.
lciukaj@splunk.com 03:38:06 ER, so… so that makes sense, I agree on that. I need to… Play with this a bit.
neil yashinsky 03:38:12 It was fun when I did, but yeah, it was easy to get started, too, just like Brew or whatever your, you know, package manager.
lciukaj@splunk.com 03:38:17 But do we have, like, lots of icons and, you know, graphics that can be used? Like, maybe something OpenTelemetry-specific, or Kubernetes-specific? I'm just wondering, or just general diagrams, like squares, circles, cylinders, and all of that.
neil yashinsky 03:38:33 Great question, I don't know the answer.
I wonder if there's, like, If there's, like, even a SIG around some of that itself.
lciukaj@splunk.com 03:38:43 I'll put maybe some comment here. Yeah.
Do we have, support, for… Altag… specific icons.
You've got peace.
I don't know, that's something to be… to be verified.
I mean, it's not something that is blocking us, but it would be nice to have, right? Or if it's not available, and it can be extended, maybe we can upload something, or build some small library, maybe that would be something also. Okay, I will put a comment. If it's not…
Available. Perhaps we can build some repo, library, Good to see.
Oh.
So, so I put it like this. Again, tool seems to be good, I like it, but if we can get something like hotel, Kubernetes, or, I don't know, container-specific, then it'll be even better. Cool.
Sounds good, let me check the board. Do we have anything else that we do? Someone else in the meantime who joined us? Because I'm not checking the list.
neil yashinsky 03:39:51 No, it's just that, metaphorically, or I guess literally the two of us.
lciukaj@splunk.com 03:39:54 I love me and you. Where are you based in, Neil, by the way?
neil yashinsky 03:39:57 I am based in Michigan area, and is my memory serving? Are you… did you, like, do, North Carolina? Did you, like, recently move or something?
lciukaj@splunk.com 03:40:04 Yeah, I'm North Carolina. I mean, I've been living here for almost 2 years. Yeah, yeah, yeah. I'm originally from Poland, but I moved to US 2 years ago, almost 2 years ago, but… but you were right about the move, but that was moved to the new house, but.
neil yashinsky 03:40:16 From one part of North Carolina to the other, not, like, first, yeah, yeah, yeah, no, the good clarification. Oh, fascinating, yeah. I mean, I'd love to, you know, I don't know how much time you have, but, like, my favorite thing about collaborating with people, period, is just, like, learning about, new parts of the world, and while my, my, understanding and documentation isn't great, I know that I have family, you know, roots or whatever, some family that spent
maybe not an insubstantial amount of time in Poland, so I know very little about it, but I've been slowly… I mean, compared to most Americans, I know a shit ton about Poland, but that's a very, very low threshold, candidly.
lciukaj@splunk.com 03:40:56 Yeah, so I'm not sure if this is a good, you know, time to discuss that, because obviously recorded calls, but I'm happy to jump on a quick call with you, maybe we're gonna have some chat. I will send you an invite on LinkedIn, if you don't mind.
neil yashinsky 03:41:09 Absolutely, no, absolutely, love to, do… just out of curiosity, if you don't mind sharing with me, like, what part of Poland did you, come from?
lciukaj@splunk.com 03:41:15 So, I was living in Krakow, which is south part of the land, so I'm not sure if you know where the.
neil yashinsky 03:41:24 A little bit. Yeah, a little bit. I've been on this Roman history, kick, which is really a European history thing, right? If you're doing it right or whatever, so… Yeah.
I love geography, I think, is just, like, a really, useful thing for me in, like, just understanding the world and people, and it's, like, that's how we kind of… there's a great intersection there. So, but yeah, next time, yeah, I'll definitely…
lciukaj@splunk.com 03:41:48 You know, connecting on LinkedIn, and then, yeah, I appreciate your leadership on the call today. I thought it went beautiful! You know, every call should be as smooth as this one went with people. Yeah, I'm excited. I'm excited about this opportunity to be part of this Blueprint initiative. I'm doing something similar with my current employer, so…
neil yashinsky 03:42:07 Oh,
lciukaj@splunk.com 03:42:08 So, I would like to also contribute to the, you know, broader open source.
neil yashinsky 03:42:12 We're sitting late.
lciukaj@splunk.com 03:42:13 So that's the reason I'm here. I'm checking now what we have… okay, agree on missing reference architectures. Okay, so this is what we just covered, right? So whether we should keep the free that we have, or we should have more, that is still
I think from my… I like this phrase that, done is better than perfect, so I'm a doer.
I like, you know, I'm, like, doing. So I'm a big fan of moving forward with the next steps, so I think that as part of this initiative, we should just move forward, and we should figure out as we go, right? Okay, do we… 100%.
At least we need to have one, we need to create a section on OpenTelemetry.io, and then we will be maybe getting more traction, more contributors to that. I remember Dan mentioned that on the last OpenTelemetry Unplugged in Europe, there was some interest in that. We'll have the Open Observability Summit in May, so maybe that topic will be covered as well, so hopefully we'll get more people involved in this, so we can either get more
blueprints, or we can enhance existing blueprints, so I'm excited about that.
neil yashinsky 03:43:18 Yeah, there… and in fact, I wonder if that's what, what is this, 2…
It's not at the bottom there. Oh, does it not have a number yet? Because it's still a draft. But yeah, I think,
The one above… no, two above that one on your screen. That one. Yeah. Yeah. I think that one was created from what is almost like a placeholder.
lciukaj@splunk.com 03:43:40 Yeah, that is placeholder, but this is 5th, so where is fourth?
neil yashinsky 03:43:44 Yeah, I don't know.
lciukaj@splunk.com 03:43:46 Because we…
neil yashinsky 03:43:47 It was… Yeah, maybe it was the one you described, but hadn't been formalized yet?
lciukaj@splunk.com 03:43:51 Could be.
neil yashinsky 03:43:53 That would… that would actually, I think, at least match the math.
from the existing… because the existing one was non-K8s, K8s, and centralized, and then the one… is… or is 245 yours?
lciukaj@splunk.com 03:44:05 Yes, 245… Okay.
neil yashinsky 03:44:07 So there is a missing fourth somewhere.
lciukaj@splunk.com 03:44:09 Yeah, there is some fault.
neil yashinsky 03:44:10 Assuming that…
lciukaj@splunk.com 03:44:11 Maybe that's a typo, but again, I agree with you, this is more like a placeholder.
neil yashinsky 03:44:15 Or, or it's, it's, it's, what's it called? Mainframe.
lciukaj@splunk.com 03:44:19 Yep.
neil yashinsky 03:44:19 I would be, you know, one of those two, I think, probably. But anyway, yeah, right on.
lciukaj@splunk.com 03:44:24 Yep.
Okay, I think we covered everything here today. So, again, I'm planning to continue working on mine, and so others, if others can, and yourself as well, can continue working on your blueprints. Then we meet in two weeks, and hopefully we have some progress here.
neil yashinsky 03:44:41 Sounds great!
lciukaj@splunk.com 03:44:42 Awesome. Thanks, Nian.
neil yashinsky 03:44:44 I was just gonna say, help me with your first name, was it Lucas?
lciukaj@splunk.com 03:44:48 Yeah, that's Lucas, that's important.
neil yashinsky 03:44:50 I mean, at least…
lciukaj@splunk.com 03:44:51 Polish pronunciation is Wukash, W-O-K.
neil yashinsky 03:44:54 Oh, gosh.
lciukaj@splunk.com 03:44:55 Yep.
neil yashinsky 03:44:55 Yes, I would love… English is Lucas or Luke, so I'm okay with it. Yeah, yeah, I wanted to make sure I remember, because you gotta, like, one tip is, like, if you change your email address from your name or whatever, it's easier for people to remember, but yes, Lucas, is that right, in Polish?
lciukaj@splunk.com 03:45:10 Lukash.
neil yashinsky 03:45:11 Wukash, I've, great chatting with you, Wukash. I look forward to catching up in two weeks or so.
lciukaj@splunk.com 03:45:16 Yep. Take care. Have a good one.
neil yashinsky 03:45:18 Take care, bye.
