SIG: End-User SIG: OTel Blueprints
Date: 2026-04-27
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Alexandre Ferreira** 00:26 Hello, Dan. How's it going, mate?
**Dan Gomez Blanco** 00:28 How's it going?
**Alexandre Ferreira** 00:30 Doing good. I just opened my camera real quick to give it a hello, but I'm quite miserable. I'm, like.
Trying to build some… some furniture.
**Dan Gomez Blanco** 00:40 Alright.
**Alexandre Ferreira** 00:42 I was in pet leave up until recently, so that's why I vanished for a couple.
But… now everything's good, and I think I joined the… the end-user SIG meeting last week.
And I didn't realize that, like, we had… we have two meetings, right? There's the end user SIG and the Blueprints one.
And… I do an APR for the Kubernetes Blueprint.
I'm just trying to find it, and I will send it, I'll send it.
**Dan Gomez Blanco** 01:29 Right. Let me start the notes as well.
Before I do that, I'm going to… Yeah, I'm going to… Make sure that we don't have any note-takers, or AI in the call.
Not everyone is comfortable with that, and we don't really… yeah.
**Alexandre Ferreira** 01:54 Yes.
**Dan Gomez Blanco** 01:54 We… the meetings are recorded, and the recordings are public, and the transcripts are available, so people can build their tooling around that.
One second, I need to claim ownership of this.
**Alexandre Ferreira** 02:18 So people are… said that I should sign the CLA before they can review it.
Create contributor versus individual contributor.
Hmm…
**Dan Gomez Blanco** 02:35 In fact, you can do that, you can do that at your own… you probably want to read the… the conditions.
**Alexandre Ferreira** 02:44 So, I see that we have T.
Hello there! How's it going?
**Tiffany Hrabusa** 02:48 Hi, Alex. Yeah, so, I was just gonna say, from Grafano's point of view, you can sign it as yourself.
You don't need to sign it, On behalf of an employee of Grafana.
**Alexandre Ferreira** 03:02 Right.
**Dan Gomez Blanco** 03:03 One sec.
**Alexandre Ferreira** 03:06 Unable to fetch user ID… That's probably because I should log in to the Linux Foundation.
**Tiffany Hrabusa** 03:29 Notes look different.
**Dan Gomez Blanco** 03:59 Okay.
And…
**Tiffany Hrabusa** 04:17 Alex, I know that you said you have to, Drop at the half past, so… .
**Alexandre Ferreira** 04:26 Yeah.
**Dan Gomez Blanco** 04:27 Alright.
Okay, cool.
Is that some topics to the agenda?
I'm…
**Tiffany Hrabusa** 04:35 Yeah.
**Alexandre Ferreira** 04:39 What's happening with my keyboard? Okay, got a steppy.
That's bad.
Hold up, I'll get another keyboard.
Compliance confirmation… I hope I don't sell myself… It should not be located in Cuba, and a bunch of… okay, alright.
**Dan Gomez Blanco** 05:50 You probably, you probably want to read those at your convenience. I mean, we can do that, we can do that later. I just wanted to, yeah, get going with the, with the meeting. Should we, review the… Let me share my screen, actually.
Okay, so if we review the board, just to make sure that we're on the same page, this is recorded, Yeah, so this has been merged now, the reference architecture template.
There's some good comments there from… From folks in the DevEx SIG.
And, yeah.
Let's now been merged.
As we said before, the current… blog posts that are being generated. They're not following this… this template, but that's absolutely fine, and, yeah.
And no, we don't expect… the blog posts, when they're copied, to follow that template either, of course.
Yeah.
So that, for any doubt, that will be in… And… here… Sorry, not here.
Oh, we should be pointing to… Actually.
I think that… not sure, maybe this is something that, we could… fix. I think this is not pointing to the right thing, they should be pointing to the issues.
In the community section, we have, review issues, but I think that seems to be pointing to projects, not issues.
So, yeah, anyway, that's us. What was I?
Right, so it'll be here, right? We've got the reference implementation template that's been… Merged.
I guess the last change that was made, just to… In case anyone wasn't following, is that we have now added… Something here that says… That all sections are recommended.
But none of them is required.
**Alexandre Ferreira** 08:25 Okay.
**Dan Gomez Blanco** 08:26 the author… this is on the reference implementation, not on the blueprint, on the reference implementation, because we want to have a low barrier of entry, for… for people to… to create them, which is, you know… So I say, share whatever you can, right? If you've got a reference implementation that you want to share from an end user, and then also added this, that authors may remove sections if they're not applicable, or if you cannot share information pertaining to that section.
But yeah, so… Now we've got this.
**Tiffany Hrabusa** 08:55 Okay.
**Dan Gomez Blanco** 08:55 It's… it's amazing.
**Tiffany Hrabusa** 08:56 And…
**Dan Gomez Blanco** 08:57 Yep. If you know any end users that want to share their implementation, that's ready to go.
**Alexandre Ferreira** 09:05 So, this probably… so, to see if I got this right, we have the blueprint template, and the blueprint states the problem statements and some guidelines.
But… and also the challenges, that each guidelines address.
And, the… I think that in my, draft, I have some implementation.
**Dan Gomez Blanco** 09:35 So that, that's… yeah, so the reference implementation is, is not related to that.
As it is related, though.
So there's two… two different things, right? One is, like, what you're… like, the blueprint that you're currently writing.
And that hasn't changed. I think if you… if you came from this template that's here, that hasn't changed at all.
**Alexandre Ferreira** 10:00 Okay, okay, yeah.
**Tiffany Hrabusa** 10:01 Yeah, I think, the connection there is that Hopefully, in the future, we will have reference implementations of actual companies that have taken a blueprint and implemented it.
And so it's very specific to their setup. It's a snapshot in time of when they wrote the document. That's how their setup was working, and The blueprint is meant to be slightly more general, so that any org or operator could come in and implement it in their own system.
**Alexandre Ferreira** 10:35 Kate.
Hello.
**Dan Gomez Blanco** 10:37 So in the reference implementation, you see things like, hey, you know, what's your organizational structure? Who's in charge of telemetry?
what's your scale, and then some of the specifics, right? Like, what config, how do you apply config, and so on. And then some of the lessons and pain points, but following that, a different… completely different, Yeah.
**Alexandre Ferreira** 11:02 So, I sent a link in the chat, which is the Kate's blueprint in my repo.
Should I refactor the implementation piece to point to future implementation guides? So this is the guidelines, and then there's implement… yeah, this implementation section, I think it's the one that makes this a little bit more complex, but should I remove this and say, hey, we are going to have future implementation blueprint, future implementation guidelines?
**Dan Gomez Blanco** 11:36 No, no, no, this is… this is great. This is, as you're, you know, as you, as you've done it. I mean, this is the intention, like, that you should have some way of implementing the blueprint. What we're looking for in reference implementations are examples, as, you know, Tiffany was saying, of, companies that have taken this blueprint and implemented it, and then what do they gain from it? You know, what's the story? It's more like, you know, that's a… Yeah.
Alright.
**Tiffany Hrabusa** 12:02 Yeah, like, maybe they encountered some issue with, you know, one part of the blueprint that just didn't work for them, and so they, you know, they did something else. Something, you know, it's going to be very specific to their setup.
**Alexandre Ferreira** 12:15 I see.
**Dan Gomez Blanco** 12:15 I think… that we could start doing, though, and… because we now have, like, three reference implementations from Mastodon, Adobe, Skyscanner, and there will be a fourth one that is… I'm not sure when that will be published, but I think there is a fourth one coming as well. There may be elements of… What you're doing, or what you're proposing, that is already mentioned in those.
reference implementations, I think it would also be okay to… to list them, there.
**Alexandre Ferreira** 12:46 Yeah.
So, I know that some of the components that I'm mentioning, like psyllium, for example, like, I asked AI to help a little bit on that, so, like, I don't know… in case that those implementations mentions those components like Celium, traffic, and all of that, we should leverage those.
And, I was talking in this end user seg, and they told… for us to chat a little bit on, like, in the PR that I've made, the last section, point to a few Grafana open source dashboards in Alrics, to monitor those components, and Like, should, like, will… Do we do that? Like, do we mention Grafana community stuff? Even though it's open source, I know they all tell wants to be as vendor-agnostic as possible. Do we think that this is good, or should I remove this section?
**Dan Gomez Blanco** 13:46 Hmm.
I think if we… if it was a… for example, in the Prometheus mix-ins, they do have a set of alerts that you can drive from Prometheus Alert Manager. That could be interesting.
however, I would probably… yeah, remove. If we're trying to become back-end… neutral. I think my vote would be to not list the dashboards, unless they're, like.
**Alexandre Ferreira** 14:23 Yes.
**Dan Gomez Blanco** 14:23 something related to Prometheus Alert Manager, maybe, but I'm not sure I would… less dashboards, unless they are, like, you know, I don't know, unless they're, like, a default standard, but…
**Alexandre Ferreira** 14:35 Yeah, yeah.
**Tiffany Hrabusa** 14:36 Yeah, I think you could just remove the dashboard column from the table, and just list the alerts that people would find useful.
**Alexandre Ferreira** 14:46 Alrighty.
**Dan Gomez Blanco** 14:46 Yeah, the Alert Registry, I think, yeah, that could be an… if it's, like, driven from Alert Manager and Prometheus and that's… Yeah, that would be useful, I think, for folks. Because… I guess it's part of the ecosystem, right? But…
**Alexandre Ferreira** 15:00 Okay, then. So, I guess that… I guess, like, I'm good on, any other questions that I have. Any other stuff, it's actually much more, like, specific to Kubernetes itself, and I will not use the time of the meeting to discuss this here. We can do that in the…
**Dan Gomez Blanco** 15:19 I think, one of the things we're talking about is… I mean, I've only started to look into it now.
One of the things that would be… that we will need here is people in the… in the collector, some of the maintainers, approvers in the collector, to… to help us a little bit with this. I spoke to Jacob as well, Because they… well, especially after they're, like, presentation at KubeCon, when they were talking about the… I guess the hotel native Kubernetes monitoring, right? So if that's something that we want to… I guess be opinionated about, and say that, you know, hey, this is how we recommend monitoring Kubernetes with OTEL.
Now that the semantic conventions are stable. I know this may delay a little bit of the blueprint, but I do wonder if, like, you know, if we want to be, opinionated about how you go around instrument in… Kubernetes with OpenTelemetry alone. And I know that Jacob was, someone else, I'm not… but Jacob mentioned that working on a… on a chart that would be, you know, basically, hey, you know, this is one way of implementing this that could help with the implementation, is… is the, the… The chart that you just deployed does.
Pretty much everything they need to do, right?
**Alexandre Ferreira** 16:46 And I… I mentioned this in the issue comment, but the… this current documentation does not leverage auto-discovery and, like, OpenTelemetry-specific annotations for the collector.
I guess that… that would be interesting to refactor, but then, like, if these other people from the collector, part, want to chime in, their opinion would be very much appreciated.
**Dan Gomez Blanco** 17:16 Yes, I think that's, you know, if that's… I think this is gonna be one of those inflection points, let's say, where we say, hey, you know, up until now.
we were… there was no official guidance, I guess, from OpenTelemetry to say, this is how you monitor Kubernetes, right? And this would be a good… plays, I think, for us to… to put together.
a… and this, you know, I just… I'm saying this here, to warn… to warn you in a bit, that it may take time for us to… to get to that You know, to go through a discussion and go, like, hey, actually, you know, we think it's a better idea to… to, let's say, stop deploying node exporter, and use the collector, like, host receiver for it, and then just deploy everything as a daemon set, and use the leader extension for… to do, like, cluster-level monitoring, and now that the semantic conventions are stable, then we're relying on those semantic conventions, so it might be a… you know, it may be a thing where, like, we want to do it right at the moment. I know that things may be changing.
**Alexandre Ferreira** 18:22 Rather than…
**Dan Gomez Blanco** 18:22 I do a template or a blueprint now, and then completely rewrite it, and… Two months, right?
**Alexandre Ferreira** 18:29 Yeah, no, I completely agree. For me, like, it's okay for this to take as long as it needs, so that we get it right on the first go, right?
**Dan Gomez Blanco** 18:39 Honestly, this… honestly, this is probably the most… I think this is… this is a critical point right now, so I've got someone at the door I need to… need to pick up.
Yep. Parse through.
**Alexandre Ferreira** 19:12 Well, probably the favorite notch, baby.
**Dan Gomez Blanco** 19:23 Alright.
Yeah, so I think, you know, it's… thanks for opening the PR, and then we can start Reviewing it and discussing the details, but yeah.
What I would like to get, like, you know, the… definitely, like, as I was reading through the… through the challenges, I think those are spot on, as in, like, you know, identifying some of the key challenges, and… and that's the… almost, like, the most critical part, is… Having that scope.
M… To, to face the… to basically, yeah, talk about solutions.
Because we'll have people, and that will come from the perspective of, I don't know.
Prometheus by Tiffany and I were just talking about that a couple of weeks ago.
I do think that there's a whole other blueprint that we can put together around Prometheus interoperability, and, like, you know, what it means, and so on. So, yeah, I think… we can start to scope things on the problems that we need to solve. And I think in this one, for example, we just… we won't be trying to completely solve Prometheus interoperability, or how… how one can deploy Prometheus and Kubernetes and collectors.
Yeah. That's the case, right, so…
**Alexandre Ferreira** 20:36 Alright. That seems good. So, I think that the current blueprint that I've put together, like.
I'm probably using knowledge from, like, one year ago, when, like, we use a node exporter and all that, and I think that we have a few other components from Hotel that generates cluster level natively, so I'll be catching up with that. I'll also sign the CLA so that everyone can review officially.
And I guess that's it then.
**Dan Gomez Blanco** 21:18 Sounds good.
Yeah, and I'll… I started reviewing it, but I'll continue with the review as well.
**Alexandre Ferreira** 21:26 Alright, so, I do have to drop, I have another meeting, but, I'll be on the CNSF Slack channel, if you need me, and I guess we'll see each other in two weeks then.
**Dan Gomez Blanco** 21:41 Awesome.
**Tiffany Hrabusa** 21:42 Thanks, Alex.
**Alexandre Ferreira** 21:43 Thank you, Dan.
**Dan Gomez Blanco** 21:48 Alright, okay, so let's move on to… other issues.
Right, so that was merged, I've… I did a PR for this. I know that, Vidya, certainly would, RESA PR, what I've done, because I wanted to wrap up a lot of this.
**Tiffany Hrabusa** 22:15 Yup.
**Dan Gomez Blanco** 22:15 aspect related to this, and then linked to… to the, yeah, so then the next one I wanted to tackle was this one, to update the guidance and architecture docs to… to explain how to contribute.
Mmm… So, yeah, I open up here, and then if Vidyat wants to… Improve it later, or add something else that can… Definitely. Not a problem.
**Tiffany Hrabusa** 22:43 Okay. Do you want me to do the… the, updating the docs, or did you want to do that?
**Dan Gomez Blanco** 22:50 I'm… I can do that, I can do that myself. I mean, I'm… this week, I'm… Sort of, like… I wouldn't say taking a week off, but, like, a… yeah.
I'm only doing hotels.
You know, yeah, not really work-related. I'm doing it on my pers… almost at my personal time, otherwise, like, you know, I've got nothing to do. So, yeah. Yeah.
**Tiffany Hrabusa** 23:10 Yeah.
**Dan Gomez Blanco** 23:10 And…
**Tiffany Hrabusa** 23:11 Well, that's good, because I have no time this week, so…
**Dan Gomez Blanco** 23:14 Good.
Mind tech.
**Tiffany Hrabusa** 23:17 And then…
**Dan Gomez Blanco** 23:19 My intention would be to, like… Have all this marched, the… this bit, and this bit.
And then create, Blog post.
And then in the blog post, what I would be doing is, like, explaining what we're doing, explaining how to get involved, and now that we've got things already open, as pull requests, I would just be basically saying, like, come and help us with reviews. Come and help us to give your opinion.
Maybe that's something that… I don't know, I said it today, but… I was thinking that perhaps… I should say it more clearly, or we, I mean, I'm just not putting that on myself, but, like, you know, that we should say it more clearly in terms of, Contributions, that these things can take time, because we're… a PR may be open, and then we'll have, like.
this is almost like, you know, when someone opens a spec issue and is open for… for months sometimes, right? It could be… it could be like that. If it's a contentious that we need to discuss, it could be like that.
and maybe.
**Tiffany Hrabusa** 24:25 Yeah, that's… that's no problem. And we can even… almost… like, post, like, a request for comments on specific PRs, too, right, on social media, like, we can say.
**Dan Gomez Blanco** 24:39 Oh, yeah.
**Tiffany Hrabusa** 24:40 you know.
**Dan Gomez Blanco** 24:41 Yeah, yeah, yeah.
I think that's a great point.
Yeah.
**Tiffany Hrabusa** 24:47 I haven't checked my GitHub notifications today, but the… the three DevEx blog posts are now in PR form. I don't know if you had a chance to look at those.
**Dan Gomez Blanco** 25:02 Yeah, I did have a look at the… My only comment is I'm not sure, and maybe we can talk about that here.
is… I'm not sure if it's possible to have, like, something like what we've got in the blogs.
that I think that's taken from the blogs, like… Type. Page type, right?
**Tiffany Hrabusa** 25:22 Yeah, yeah.
**Dan Gomez Blanco** 25:24 Yeah.
So I'm not sure if it's, like, possible to do that.
There's no. I don't…
**Tiffany Hrabusa** 25:30 Yeah, I don't know either.
**Dan Gomez Blanco** 25:33 Yeah, if someone knows how to configure Hugo… is it HugoDocs that we use, right?
Yep.
To treat a page like a blog in terms of template or format, and that's… Great. If not, then I guess we can just almost, like, replicate it, right?
Like, something like that.
**Tiffany Hrabusa** 25:52 Yep, do you want this for the blueprints as well, or just the reference implementations?
**Dan Gomez Blanco** 26:00 I think for both. I think it would be good to have it for both.
**Tiffany Hrabusa** 26:05 Okay.
**Dan Gomez Blanco** 26:09 Yeah.
**Tiffany Hrabusa** 26:12 Okay, I will check, with… The infrastructure experts in… Coms, and and let you know.
**Dan Gomez Blanco** 26:22 Sounds good.
Yeah, and then in terms of the… Order.
I personally like alphabetical, because it's not a blog post, or it's not a blog.
Yeah, I guess.
If I were to look, because all of them would be company… company name, Colin… Something else, right?
So, I guess if I were to look for reference implementations, I think I would probably be… Scanning through the list of… companies. Users, for the end users.
**Tiffany Hrabusa** 26:55 Okay, that makes sense to me, too.
**Dan Gomez Blanco** 27:00 Cool.
**Tiffany Hrabusa** 27:00 Okay.
**Dan Gomez Blanco** 27:03 talks.
**Tiffany Hrabusa** 27:06 So is there anything you need me to do this week, other than the two?
Action items in the agenda?
**Dan Gomez Blanco** 27:14 Nope I will be doing as much as I can in terms of, yeah, creating the blog post, and… and then after that is when I will… Finally focus on the blueprint that's assigned to me.
**Tiffany Hrabusa** 27:31 Okay.
Alright, that sounds good to me. I will, I'll watch for your docs PR.
to update with the how to contribute, so we can get that merged, right away. And then…
**Dan Gomez Blanco** 27:47 Yeah, it depends on the idea as well. What I was thinking is to have, Gives me shatter.
To have a… To basically just do, like, a separate… like, a section here, like, how to contribute.
And this one?
And then in maybe each of these ones, say, if you want to know how to contribute a link to the… rather than rewrite it twice, because it will be this… it will be pretty much the same process, in terms of, like, raise an issue in the end user seg, you've got the templates here, and all that.
I'll just basically link from these ones to the… To the main one.
**Tiffany Hrabusa** 28:32 Yep, that works.
**Dan Gomez Blanco** 28:34 Cool.
Awesome.
Okay.
So, yeah, I think we've got some work. I've not really had a chance to look at Lukash.
PR either, but yeah.
Make some time for that as well.
**Tiffany Hrabusa** 28:55 There's a lot of triplet sentences.
**Dan Gomez Blanco** 28:58 Alright.
Okay.
**Tiffany Hrabusa** 29:03 It started melting my brain after… I commented on that, too.
**Dan Gomez Blanco** 29:07 No, I'm becoming allergic to it a little bit, to be honest.
It's like, I just get this, like, yeah.
**Tiffany Hrabusa** 29:16 writer.
Yeah. But, I think otherwise, I think it's… it's pretty good, so… But yeah, I will…
**Dan Gomez Blanco** 29:25 have you seen the Wikipedia, like, guidance, I think it's great.
**Tiffany Hrabusa** 29:30 No, I haven't.
**Dan Gomez Blanco** 29:31 I'll send it to you, it's a really, really good document.
Yeah. Alright.
**Tiffany Hrabusa** 29:38 Alright.
**Dan Gomez Blanco** 29:38 Possibly.
**Tiffany Hrabusa** 29:40 Thanks, Dan.
**Dan Gomez Blanco** 29:41 Alright, thank you, bye-bye.
**Tiffany Hrabusa** 29:43 Bye.
