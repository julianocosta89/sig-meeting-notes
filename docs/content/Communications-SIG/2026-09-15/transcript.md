SIG: Communications SIG
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marylia Gutierrez** 00:37 Hello!
I like the background.
Oh, you're muted.
You're still muted.
**Severin Neumann (Bronto)** 00:58 I'm actually right now in my… hey, everyone, I'm in my… how do you say this in English? Like, washing… washing room, washing kitchen?
Because, like, I…
**Marylia Gutierrez** 01:07 laundry room.
**Severin Neumann (Bronto)** 01:08 a few things.
**Julia Furst Morgado (Dash0)** 01:08 Laundry, yeah.
**Severin Neumann (Bronto)** 01:10 Let me put on a pretty, pretty background.
**Julia Furst Morgado (Dash0)** 01:15 I like it.
**Severin Neumann (Bronto)** 01:17 Awesome.
Hey, Julia, hey, Vivek.
**Vivek Anandaraman** 01:20 Good.
**Severin Neumann (Bronto)** 01:21 Good to see you.
**Julia Furst Morgado (Dash0)** 01:21 I… Nice meeting you, Vivek.
**Vivek Anandaraman** 01:27 Nice meeting you, too.
**Severin Neumann (Bronto)** 01:29 It looks like we're a few more people than last time.
I don't know, maybe we wait another one or two minutes for everybody to come in, and then we can get started. If you have anything for the agenda.
You can… Still updated.
Let me put it into the chat.
I can also see if I can… Share it with you… Okay, I think you should see my screen now.
**Marylia Gutierrez** 02:06 Yeah.
**Julia Furst Morgado (Dash0)** 02:08 So, yeah.
**Severin Neumann (Bronto)** 02:09 Maybe also add your name here if you want to, this is not.
**Julia Furst Morgado (Dash0)** 02:13 augmented.
**Severin Neumann (Bronto)** 02:13 But you can.
**Julia Furst Morgado (Dash0)** 02:15 Understood.
**Severin Neumann (Bronto)** 02:16 here.
**Julia Furst Morgado (Dash0)** 02:16 Severin question. The topic you added, getting started project, is that the same one, of the reference application?
**Severin Neumann (Bronto)** 02:28 I… I… yeah, this is… this is part of it, yeah, yeah.
**Julia Furst Morgado (Dash0)** 02:31 Okay, that… the one that you sent me.
**Vivek Anandaraman** 02:33 Infinity.
**Severin Neumann (Bronto)** 02:34 Yeah, I… exactly.
That's the one I mentioned.
**Julia Furst Morgado (Dash0)** 02:37 I was gonna ask about it. Cool, thank you.
**Severin Neumann (Bronto)** 02:40 Okay, yeah, let me maybe actually, in the background, Rick, Rick, open up some links or it… While we wait… but I think… I'm not sure if anybody else joins, I think… Patrice said he's not here. Hey, Vitor!
Good that we waited for a little bit.
Should I just do here?
Okay, cool.
Does anybody else have any topics they want to add? If not, I can just start with mine.
Thinking this is a no. Okay, let's talk about the registry and ecosystem pages. We wanted to talk about this for a while. Just to update everybody once again, so a few weeks back, we decided to… freeze them, and then think about, like, okay, how to move forward with that, and then what are the next steps we want to take with them.
For those of you who have attended the maintainers call that was, like, an hour ago.
Also collected a little bit of a feedback Especially on the registry. I think we did not even talk about any of the vendors, integrations, and adopters pages.
I think the most interesting… or there were, like, two kinds of feedback.
One was, like, hey, there's people actually using it. I think it was Jason, especially, who said, like, hey.
We, we, we, I, I recommend it to… to salespeople and technical.
Or professional services people to look up what is out there, and what they can use, and what they can find.
So this is definitely a good number, and Michael confirmed that this is a thing.
And then there was a little bit of conversation around, like, hey.
how could this, like, move forward? Like, how can we integrate it into the ecosystem Explorer, or is there any intermediate solution that we can take?
So yeah.
Before I… before I go on with anything of that, any… any questions, any comments on that from… from… from anybody else?
Making this as a no. So, Okay, I think for the registry, I think my feeling is, and Jay and Vitor, since you're here, you might know this better. I mean, long-term, we want to… we want to replace it with the Ecosystem Explorer, right?
But, like, putting a timeline on it is probably not something… easy to do right now. So I think the big gap that we still have to close is, like, what are we doing in between, right? Are we just throwing the registry out and tell people, like, hey, this is not a thing anymore, or can we find a way To… to keep it… Simple for us.
But at the same time, like, yeah, not… not… not go away with it, so to speak. So, yeah.
**Jay DeLuca** 06:24 Yeah, I think, like… Before we can even start to move forward with it in the Explorer, we need to define the bar, because I think that's kind of the thing that we need to incorporate in the new evolution of this, is, like, what justifies including it in the registry. I think we need to… Set some boundaries and not expect it to be the… everything that touches OpenTelemetry is listed here. It's… it's… it's a more… fine-grained of, like, anything that implements OpenTelemetry that can pass these gates of whatever sort.
But yeah, we just… I don't… I don't have any idea of how quickly we could get something like that stood up.
I think the best thing that we can do is, at least from the Explorer side, is really focus on the conformance piece, and as we build out each ecosystem, like, really push… To have that as a first-class citizen of… some way of proving that these components conform to semantic conventions, as an example.
But yeah, I don't… I don't know, I, like… we could… we could set up automation to try and alleviate some of our review burden and keep the existing things going for a while. Maybe we put up some banners that give some caveats of, like, hey.
You know, this… the information in this registry is not kept up to date, it's crowdsourced, you know.
Proceed with caution. Yeah, I don't know, it's, I think, like, adopters, is that even… Like, if we just look at what's here, I mean, vendors… And adopters, I think, are, like, probably the less important.
ones, like, I doubt that somebody's like, oh, I want to use OpenTelemetry, I'm gonna go to this vendor's page. I mean, maybe they do, I don't know.
And then the adopters, I think that's great, in terms of, like, as we were approaching graduation, but I don't know that we necessarily, you know, need it.
**Severin Neumann (Bronto)** 08:36 I mean, we are beyond graduation, right? So yeah, I mean… I mean, in my mind, adopters… so this is the one where I was really thinking about, like, hey… so if we… if we compare this with, like, Kubernetes, right? Let me… What did I do?
they have here… where is it?
They have somewhere case studies.
Thanks.
There you go.
Right, that's how they… oh, no!
**Vivek Anandaraman** 09:14 Okay.
**Severin Neumann (Bronto)** 09:14 They even link this now out to the CNCF, is this correct?
It's interesting, actually.
This is some new… So this is actually also an interesting approach. So they link out to… case studies by the CNCF now.
And ZLIK, I mean, yeah, you could probably pre-select open telemetry here.
And they're like, okay, this is now… This is now… our adopters page. That's actually an interesting one. I have not even thought about that option.
Meet… Take not a math.
And if we now look at… I mean, integrations is kind of taking from the registry, right? So this was more a place to highlight projects.
that have first-class support for OpenTelemetry, right? This is… this is the one page I personally would miss the most.
Because it feels like this thing where we can say, like, hey, look, all those projects, you make use of OpenTelemetry natively.
But then we remain with distributions and vendors. I mean, and distributions, in my mind, like, we could just get rid of it entirely.
I'm not really exactly sure what the value of it would be, beyond the, like, hey, certain vendors have their own distribution.
And the vendors page, I mean… yeah.
is also… a long list of names, and here, even more, like, the thing is, like, I could name a few here, probably, that no longer exist, or if we click on any of those links, we just land somewhere.
somewhere that, so… here was the proposal, I think, by Jack to say, like, hey, why not have, like, more, a page of vendors that support OpenTelemetry and contribute to OpenTelemetry, which led people to create a Reddit post about it, and they're like, hey, this is not fair, which is its own debate, probably.
But yeah, maybe that's another one. But… and the registry itself, I agree with you to make it long, Jay.
maybe we just need to figure out a way how to make it a little bit more sustainable while the ecosystem Explorer is evolving.
Yeah.
**Jay DeLuca** 12:09 Maybe we just, for now, we unfreeze it?
And we try and optimize our approach, and maybe it's something that, like, we merge bi-weekly or something, like, it's not even… you know, something that we stay on top of.
And then, yeah, in the long run, we try and come up with, some… Better criteria for these?
**Severin Neumann (Bronto)** 12:35 Maybe something like that, that we say, like, hey, there's PR, so maybe only merged once per month, maybe even that.
And the other thing is, like, maybe we reduce it down to, like… because what I hear, like, what people actually are, like, like, if you look like, right, I mean, we have here, like.
**Vivek Anandaraman** 12:51 Right.
**Severin Neumann (Bronto)** 12:52 a bunch of things, right? But what people actually care about is, like, instrumentation libraries.
and collector components. But this whole, like, utilities thing here, Which… yeah, also grew… significantly.
This may be something that we should…
**Vivek Anandaraman** 13:13 education.
**Severin Neumann (Bronto)** 13:13 get rid of.
To some extent, so that we say, like, hey, all you can add in the future are instrumentation libraries and collector components, and everything else is just frozen, and we will not change it anymore, or we even remove it. I mean, that's an option that we just reduce the surface drastically.
Yeah.
**Jay DeLuca** 13:38 I think one other thing is, maybe we have a specific form that they need to fill out that make… I mean, we won't check it, necessarily, but, like… you know, my whatever component, you know, implements the correct API, or, you know, just some kind of… like, form for them to go through and say, like, yes, my library does this stuff, because I think a lot of people don't even know.
like, what semantic conventions are, and they build, like, an instrumentation library, and they say it's OpenTelemetry compliant because it emits OTLP, but it's not, you know, conformed.
So, yeah, I'm just trying to think of, like, even if it's… whatever… more burden, maybe that's not the right word, but, like, level of effort required on the, submitters that doesn't also require additional effort from our end, could also help, maybe.
Improve the quality and reduce the blast radius, but…
**Severin Neumann (Bronto)** 14:42 You mean, like, a form in the GitHub, PR?
**Jay DeLuca** 14:44 Yeah.
**Severin Neumann (Bronto)** 14:45 Provide or dedicate, like, a separate one that they need to fill out.
**Jay DeLuca** 14:49 Like, yeah, like, just have a template, a PR template, or an issue, like, or… I don't know, something like that, maybe… I'm not sure the mechanics of it, but yeah, just, like, if you want to add to this registry, you just have to fill out this form of explaining why it should be added, essentially.
**Severin Neumann (Bronto)** 15:07 Yeah. Yeah. No, I think that's a… that's an interesting point as well.
So you mean, like, pushing down some of the burden to the people, and if they don't fill out this form properly, we don't even, like, take a look into it, or maybe can have an AI run over it and say, like, oh, this is not what we're expecting, or something like that.
**Jay DeLuca** 15:28 Yeah, and even just to kind of start communicating the expectations we have for components that we consider to be part of the ecosystem. That they follow the specification, or they follow semantic conventions.
**Severin Neumann (Bronto)** 15:40 Wow.
Yeah, yeah, yeah. That is an interesting one.
Yeah, let's maybe, maybe think about, like, doing… let me add note on that as well, real quick.
**Jay DeLuca** 16:08 Like, maybe we could have a GitHub action that, on any PR that's open that has a registry, it, like, adds a comment to the PR that says, hey, if you're adding You know, to the registry. These are, you know, if you're… if it's an instrumentation… You know, make sure that you're… following semantic conventions, maybe we just, like, link out to the documentation around that area. If you're building an SDK, you're following the specification. If you're omitting telemetry, you're omitting proper OTLP. Just like these high-level, basic things.
We can link right to documentation.
And then, yeah, they just have to, you know, if it's applicable to them, they have to check it off.
But yeah, it doesn't add any more work, and it starts to kind of encourage them to make sure that they are actually creating, like, quality native components.
**Severin Neumann (Bronto)** 17:02 Yep.
Yep.
I mean, the only thing I struggle with, of course, this puts back a lot of burden on the maintainers, right?
So the one thing I'm still, like, someone proposed it, I cannot remember who, is that, like, maybe we put that whole thing out into its own repository, so that way it's a little bit more clear, like, yeah, who is taking care of it and who is not taking care of it.
And we have it not… being among the hundreds and hundreds of PRs that we have right now in the otel.io repo.
I'm not sure if this is really helping, so I'm wondering how people think about that idea.
**Jay DeLuca** 18:01 I mean, it still requires us to get people to… To volunteer to manage it.
**Severin Neumann (Bronto)** 18:09 Yeah, well, we have it there, and people see, like, nobody's taking care of it, so… I don't know, so maybe it makes it a little bit more obvious that it's… That it's… that it's not taken care of by a lot. Or we can hand it to people without making them, like.
Giving them full access to maintaining io repository, right? I mean, there's people that care about the registry, I don't know.
Any…
**Vitor Vasconcellos** 19:00 adoption.
**Severin Neumann (Bronto)** 19:02 Sorry?
**Vitor Vasconcellos** 19:03 Nope, that's a good option, this… This last one.
Moving to a separate repo.
**Severin Neumann (Bronto)** 19:12 Because, yeah, because that way we can really say to people, like, hey, if you really care that much about the registry, here's, like… here's, like, what you can do to help work on this repository, and… but… but be… I mean, the only thing, again, is, like, they need to be aware, like, hey, eventually this will go over into the ecosystem Explorer.
So… so that's the only risk that, like, we… we create… we create some… The workaround it becomes a permanent solution, right?
**Jay DeLuca** 19:47 I mean, we could… hypothetically, if we spun up this separate repository and we had, like, a dedicated team of people, they could potentially start building in automation tools to verify that data.
We could still publish it in the existing registry, and we could also consume it in the Ecosystem Explorer and start to build on top of it if we wanted.
Yeah, I think it… it… I don't think it solves the problem unless we get another Because I think the issue is none of us want to maintain this, right? So, like, I think this is a good idea, assuming that we are able to recruit people, and maybe that's what we try to do, maybe we… like, would we need to put together a proposal for it? Because the other thing is, like.
Yeah, if the ecosystem's gonna… Ecosystem Explorer is gonna replace us at some point, we don't want to put too much effort Or we want to just make sure that there's… there's synergy there. I don't know.
**Severin Neumann (Bronto)** 20:52 Yeah, yeah, let's… let's keep that open as a floating idea. I mean, the good thing is, like, from my point of view, at least, we don't need to make a decision immediately, right? I mean, we can still wait a few days or weeks, and see, like, how it evolves.
**Jay DeLuca** 21:09 Yeah.
**Severin Neumann (Bronto)** 21:10 But yeah.
Yeah, let's… let's maybe leave it like that, or is there anything else that anybody wants to add to… to that debate?
Nope.
Okay.
Then let me get back to the… to the second topic.
Some of you might noted, like, a few… Month is probably… The wrong term.
It's… Maybe 2 years ago, something like that.
I brought in a proposal that we think about doing a new getting way of how we do getting started with OpenTelemetry, right?
And one key building block of that would have been, like, that we said, like, hey, we build a reference application Across all the languages, So that then we, upstream, in the documentation, can use that to build out… to however structured getting started, right? So we say, like, hey, every SIG owns… an example application… that exists not instrumented, that exists instrumented, and then we can use that to guide people through the process to, like, hey, how do you go from that one app to the other app? Or maybe even if the uninstrumented exists… one exists, maybe even things like, hey, if you use any kind of automatic instrumentation.
how can you, like, even, like, use that? But unfortunately.
That project, lack of probably also my own bandwidth, never, never… got any far.
So, so I'm thinking a lot about, like, hey, how can we… How can we… reignited also with, like, the light of deadlight. We have the Beginners for OpenTelemetry video series right now, and then there's, like, a few places where we think about how to get started with OpenTelemetry, how can we maybe even bundle those things, right? How can we… how can we yeah, think about that, because this is still, I think, one of the biggest feedbacks that we get for OTEL, that, like, getting started with it is sometimes, like, really complicated and… not straightforward.
I mean, at the end, it boils down to the same problem with the registry, right? I mean, we maybe need to… and someone… that's, by the way, something we should add to the section above as well, like, that we should do a blog and a call-out to say, like, hey, we need people People are interested in contributing to that.
So, yeah.
**Jay DeLuca** 24:44 It could always try and leverage, like, the LFX mentorship, if somebody here was willing to… To be, like, the mentor and put together that project.
**Severin Neumann (Bronto)** 24:59 I, I, I… I think that the main thing is to have a maintainer that, like, owns it, right? Because I would love to own that one, but, like, I cannot really make the bandwidth for it.
So I would love to see some people say, like, hey, I'm more than happy. Because a lot of the work that needs to be done here is, like, really also stay in sync with the different SIGs, right? I mean, we have a few SIGs that started implementing that, or we had a few people, like, reaching out to different SIGs and say, like, hey, I want to implement that, but they sometimes got lost because, like.
I didn't follow up, or anybody else did not follow up with them, and then, of course, they lost interest and attention to it.
So yeah, I think that the main thing would to have maintainers that are curious and excited about it.
**Julia Furst Morgado (Dash0)** 25:50 So, I was gonna say that, I'm happy to help, in any way I can.
But from what I understand, you want someone, or more than one person, to lead this project, right?
**Severin Neumann (Bronto)** 26:06 Yeah, yeah, yeah.
So the one thing is definitely we need people to, let's say, take care of the implementation, but we need also people that say, like, hey, I own this thing, and then I make sure that it's pushed forward, right?
**Julia Furst Morgado (Dash0)** 26:21 and talk to the SIGs and make sure that they are helping as well.
**Severin Neumann (Bronto)** 26:29 Yeah.
**Julia Furst Morgado (Dash0)** 26:29 I'm… yeah, I'm gonna take a better look at what you sent me. I was just reading about it before this meeting, but I'm interested, so I can be one… one… one of the people that, you know.
can start leading this, and, and try to find other people, because I think, like, just myself, it's not, feasible, but definitely, I'm happy to… to start it.
**Severin Neumann (Bronto)** 26:58 Okay, that's really cool, and happy to hear that. And as you said, like, this is definitely something where it would be good to have maybe one or two people more. And I mean, I'm not, like, not, like, hands-off on that, like, I'm more than happy to Help you… help you.
**Julia Furst Morgado (Dash0)** 27:14 Dad.
**Severin Neumann (Bronto)** 27:14 but it's just for me, like, keeping an eye on all the PRs, keeping an eye.
**Julia Furst Morgado (Dash0)** 27:18 Yeah.
**Severin Neumann (Bronto)** 27:18 things, like, it would be really good to have someone who's just like, hey.
every week, I think about how to make progress here, right? If this isn't something you can sign up for and find maybe one or two more people to do that, then this would be really helpful.
**Marylia Gutierrez** 27:35 I was gonna say, also, maybe… kind of related, like, blueprints that there were, like, people seeing, like, how to get started on specific type of instrumentations. That is something that, like, maybe can probably get in contact with them and see if there's any collaboration that also can be done.
**Severin Neumann (Bronto)** 27:58 Okay, so you mean that in the Blueprints Project, If they're interested to collaborate on that, to say, like, hey.
**Marylia Gutierrez** 28:10 Yeah, also, like, you should not confuse people, because we are saying, like, oh, this is how you get started for, like, these cases, but there is also the blueprint saying, like, hey, this is how you actually implement on those cases, so they're like, why? They're, like, two separate things? What is the difference between those two implementations. So… I think they… those are two products that should be somehow aligned?
**Severin Neumann (Bronto)** 28:41 Yeah, I mean, just seeing those reference implementations, they're probably also case studies to some extent. So yeah, we should make sure that… but yeah, I mean, blueprints are more like…
**Vivek Anandaraman** 28:54 Okay.
**Severin Neumann (Bronto)** 28:55 Complex environment.
**Marylia Gutierrez** 28:57 That's fine.
Yeah, yeah, I think, like, this one you're talking about is very, like, how to get started, very basic. Blueprint is more like, you have a hundred things at the same time, how do you connect all of them?
**Severin Neumann (Bronto)** 29:09 Yeah, exactly.
**Marylia Gutierrez** 29:09 But I'm just saying, but I'm just saying, like, from somebody who doesn't know, and they are entering here, and they're looking, so they're like, why do I have this getting started? Why do I have the blueprints? So make sure that, I don't know, we have… Something more, like, aligned. Like, the flow makes sense for whoever's using.
**Julia Furst Morgado (Dash0)** 29:27 but also.
**Severin Neumann (Bronto)** 29:27 Oh, maybe…
**Julia Furst Morgado (Dash0)** 29:28 we can have a call out and say, if you, your organization already has several services, go check out the blueprints. Blueprints are ta-da-da-da-da-da. This is for, you know, so, be specific for who, who that is, the Getting Started project.
**Severin Neumann (Bronto)** 29:54 I'm just adding… Yeah, I'm here. Yeah, no, that's definitely a good point, that this team and this… is it a SIG? Like, is Blueprints a SIG, or is it, like, a sub-project of… And you're so sick, I'm not sure right now.
**Marylia Gutierrez** 30:15 It's kind of like a sub-project, like, working group, or SIG, or whatever, because even, like, the calls are within the end user.
**Severin Neumann (Bronto)** 30:22 Okay, yeah, but even that, like, I mean, the whole getting started thing, I mean, to some extent, sits with end users, right? I mean, this is, like, the whole video series, and something like that. So yeah, maybe we reach over to end user SIG SIG end user.
**Vivek Anandaraman** 30:40 Right.
**Severin Neumann (Bronto)** 30:43 If, if they are, like.
**Vivek Anandaraman** 30:45 Excellent.
**Severin Neumann (Bronto)** 30:46 Having… having some overlap there, and so, like, hey, this is something we would be interested in helping with.
That's a good… that's a good call-out.
**Vitor Vasconcellos** 30:59 at some point earlier this year, also, I… I mean, I'll send it here, but let me add to the document as well.
I created this… these other… This other view that would overlap with the demo SIG.
And then the idea was to implement the reference application, but also have a… Eye… A walkthrough, based on… language, or Sinos, or anything that… Changes the result.
And… Yan… The… the user could have, A basic implementation on… On what they are trying to do.
But, yeah.
**Severin Neumann (Bronto)** 31:50 I think, yeah.
**Vivek Anandaraman** 31:51 Yep.
**Severin Neumann (Bronto)** 31:53 No, no, go ahead. No, no, go ahead, sorry.
Yeah, I don't know already.
**Vitor Vasconcellos** 31:58 Yeah, I think this… we have some limitations with the… Framework, the website's currently running, so… I don't think this would… actually work well.
But… yeah, that's… there are some resources also for references.
**Severin Neumann (Bronto)** 32:20 I mean, if we feel like, for this getting started, that, like, hey, maybe we need to fork this out from Google into something more interactive like that.
I mean, this definitely comes with certain challenges, right? Let me say this upfront for sure.
but if we think that's the way to go, Yeah, why not? I remember that, like, for some… but it was not Kubernetes, I think it was… it was one of those local clusters that you can run. I think they also have something like that, where it's much more interactive.
how to get started. Was it kind, or was it… Was it the other one?
one of them had this very interactive way how to get started, and I think we could have something like that as well. And if we think about, like, hey.
Is there a better place to… to fork it out from the classic Hugo environment.
Then let's have at least a discussion about it, right?
Good day you brought this up, Peter. Thank you.
**Julia Furst Morgado (Dash0)** 33:25 If I may say, I think for beginners, an interactive thing is definitely easier to understand. So I think we need to… to talk about who is the audience for these getting started.
beginners that don't know anything about OpenTelemetry, or people that know some, OpenTelemetry, and, you know, they… they are using already one language, and they want to learn more. So, depends. If it's, like, new new, definitely what Vitor was showing, what he started building, is more helpful.
**Severin Neumann (Bronto)** 34:04 Yeah.
**Julia Furst Morgado (Dash0)** 34:10 Because I think people that already know about OpenTelemetry, they know how to get around the documentation.
**Severin Neumann (Bronto)** 34:18 Yeah.
No, and I think at the end, there needs to be, like, I think we… this was what especially the Java SIG did at some point, is that, like, they forked out this whole thing of, like, hey, here's a reference documentation, and this is much more… Around getting, getting, like, deeper, and then getting details on, on specific things. And the… and the getting started is more like this.
this small… this small subsection here. So… so here, our getting started, I mean, we technically had to think to say, like, hey, you're DAF, your ops, here's what you should be learning.
I mean, if… we had this proposal a few times, I also remember that Jurassi brought something like that up back in the past, that there's some, like, cool things where people have some very interactive ways of learning how to get started with OTEL.
So yeah, maybe, maybe that's definitely something that… that maybe… Can and should live at a different place, but yeah, right now, we mainly need people that say, like, yeah, we care enough about that, and then take care of it, and then drive it forward.
**Julia Furst Morgado (Dash0)** 35:31 I do.
**Severin Neumann (Bronto)** 35:33 Yeah, thank you.
**Julia Furst Morgado (Dash0)** 35:34 So yeah, count me, and…
**Severin Neumann (Bronto)** 35:39 Awesome.
Yeah.
That's a lot of good feedback on this project.
that's all we have on the agenda right now. Is there anything else anybody wants to… Chat about anything?
Yes, no, maybe?
And I thank you, everybody, for taking the time, giving your back.
some 25 minutes, and talk to you on Slack, and then in two weeks from now.
**Jay DeLuca** 36:14 Bill.
**Severin Neumann (Bronto)** 36:15 Thank you, bye-bye.
**Virginia-Diana Todea (VictoriaMetrics)** 36:17 Bye.
