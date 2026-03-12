SIG: Go Auto-Instrumentation SIG
Date: 2025-10-28
Duration: 10 minutes
Zoom Recording URL: https://zoom.us/rec/share/1ArthsfWN-Sr2_jNZ3EYz8xCYcgz-8dpuY58xcCL1nZ3QqxUJ4PPkmiO9_st44yD.yPXFoWKw3AllZ4O3
============================================================

## Zoom Recording Transcript

**Tyler** 01:07 Hey, Ron, how's it going?
**Ron Federman** 01:12 Hey, doing good, how are you?
**Tyler** 01:14 Doing well, yeah.
Did you say you're making it to KubeCon, or is it just your coworkers?
**Ron Federman** 01:25 Yeah, yeah, I will be there. But, not on… like, my flight is on Sunday.
I'm not.
**Tyler** 01:31 Oh.
**Ron Federman** 01:31 icon.
**Tyler** 01:33 So, not the maintainer's meeting?
**Ron Federman** 01:35 Yeah.
**Tyler** 01:36 Okay.
But you're gonna make it to the observability Day, then? On Monday?
**Ron Federman** 01:41 Yeah.
**Tyler** 01:42 Okay, cool, cool.
Yeah, well, I'm sure I'll see you around the booth at the very least, if not, you know, at the talks, yeah.
**Ron Federman** 01:52 Yeah, I saw you, you have a talk with Nicola, right?
**Tyler** 01:55 Yeah, yeah, we're gonna, talk about, troubleshooting, production incidents, or just how you can use, like, eBPF systems, or OB, or all this, eBPF instrumentation we've developed for Yeah, just troubleshooting things and finding things out. It's cool. Yeah, I've… if I'm giving talks where it's like… I, like, I don't know, like, I don't know if this has never happened, because it seems like it always happens, but it's like, I always prepare a talk, and I'm like, I think that's a cool talk, and then I go and build the talk, and I'm like, oh, wait, this is actually, like, way cooler than I thought it was.
**Ron Federman** 02:33 It definitely happened, like.
**Tyler** 02:35 Was it, like, last year?
I can't remember, I think it was last year, I gave a talk with Mike Dame as well, at DevConf about, the work we did in this project. Yeah, yeah. And I remember, like, halfway through, like, getting ready to give the talk, I had, like, just finished the demo, and I was just like, man, this is actually really cool, like… It's funny, like, how you can always be surprised when things are cooler than they actually are, like, are cooler than you think they're going to be, so, yeah.
**Ron Federman** 03:06 I will try to… I will make it to this, this talk.
**Tyler** 03:10 Cool. Yeah, yeah, I'd love to, love to have a good audience.
But yeah, it looks like there's a few good talks. I think, Mario as well from Grafana's given a talk, on, some of the OB work as well, and then… Yeah, obviously there's, like, the whole…
**Ron Federman** 03:30 three talks, yeah.
**Tyler** 03:31 Yeah, yeah, there's a ton of those, so… It should be good. And a lot of them are at the main conference, too, so it's not like it's just relegated to the observability Day. I mean, obviously, the observability's gonna be great as well, but yeah, it should be… Should be pretty good.
**Ron Federman** 03:46 Can't.
**Tyler** 03:52 Let's see, where are we at? Oh, we're almost 5 minutes in. I didn't have too much to talk about.
I did have… one item… that I've just been looking at in the background. I've been pretty busy doing a bunch of other things as well.
But, one of the things that we, you know, we're trying to do this integration still, with the… Sorry, let me just… Maybe share.
I'll share my notes really quick.
Yeah, so we're just trying to, like, one of the things we're trying to do is unify this project with the Obi project.
And, obviously, like, we had talked about, like, a phased approach, being that we're gonna try to, like, work at the probe level, then work our way up through the instrumentation, but one of the other things that I've noticed, There's a little bit, like, you know, we can do in parallel, is this unification of, like, this offset generation.
So I've just been looking at, like, refactoring the offset package, or creating a new offset package or something like that. Like, essentially, like, extracting what we have, in, like, a few different places and putting it into, like, a unified, like, public, package.
with, like, a public API, that we would then just start using that, and, hopefully Obi would start using that. The goal is, like.
also, not only Obi, but, like, possibly other, third-party, people would start using that, just because, like, we would be supporting custom probes eventually, and so we would want to have, like.
Obviously, we still support, like, offsets on the fly, but it's nice to have the caching, mechanism, so… Yeah, so the idea was, is, like, you know, if we can make this unified across the two projects, which should also work across, like, third-party, you know, groups that are also using this, and they could provide their own offsets file.
was kind of the idea. So, yeah, I'm just looking into refactoring this. It's something I had worked on before, so I felt like it was positioned for it, but it's not a, it's not a, like, top priority, so I'm just kind of working on it in the background, but yeah.
**Ron Federman** 06:02 Yeah, I think it's a… like, it's a great idea to have as much as… common stuff as possible. Like, this offset stuff, It's… it's, like, even not really much Go-specific, like, there's… you know, with just the Go packages that we look for, but all the binary parsing and… Building the offset table and all those stuff, it's like… it can theoretically be used for other languages as well, I think.
**Tyler** 06:35 Yeah, that's a good point.
Yeah, because, like, what we have right now is very ghost-specific, so… maybe that's something to keep in mind as I work through this, is, you know, how do you also define, like, those templates that we're using to look for specific symbols, like… Generically enough where it could work with, you know, a bunch of other, you know, languages, or any sort of binary that you want to hand it. I mean, obviously, that's another thing, is like.
it's not gonna work for, you know, dynamically compiled languages, but… Right. Yeah, like, yeah.
But I think that, like, for all of the other, like, statically compiled binaries that we can hand it, we should be able to say, like, pull an offset out of here, and it should work. So, yeah.
**Ron Federman** 07:19 Yeah, like, the part that we, like, parse the binary to figure out, like, where the offsets actually are, that's… that part is, like, the same for a lot of languages, I think, like, the debug format in the binary.
Yeah.
**Tyler** 07:34 Yeah, right? I mean, that's… that's the whole point of, like, that whole section of the binary, is that it's standardized, right? So, yeah. Yeah.
So, yeah, so, yeah, I think that's a good goal, actually, in this refactor, to make it general enough. Like, I already wanted to make it general enough that where, like, a user could provide their own… like, templates or something like that, but, like, maybe… or I, like, yeah, like… provide some sort of, like, way to get a binary, and then from there, ask where that, in that binary it should be, so… Yeah, I… you know, and then obviously, on top of that, you also want a unified way to get some sort of, like, indexing system on top of it. So, like, once you have… You know, it discovered the offsets, you want to store them in some sort of way so that, you know, it translates into some sort of, like, caching thing that you can persist to disk.
then you want to be able to load that cached thing back. Like, those are kind of, like, the big high-level functions. And then, you know, just rethinking that as we go to move this into, like, a public package so that it becomes, yeah, I think a little bit… More general, but also user-friendly and accessible outside of the project, yeah.
So… Yeah, like I said, I was gonna create an issue for it, but I just, I've just been prototyping, so I, like, I haven't… I was, I guess, more running it by this, just to see if it was worth, pursuing, and it sounds like it is, so I can probably create an issue to try to track the work as well.
But… Yeah, just a… just a heads up on… on that.
But yeah, other than that, I didn't have too much else to talk about.
Anything else you wanted to discuss, Ron? I don't think… There's too much more going on.
**Ron Federman** 09:18 And… no, I'm… Don't have anything.
**Tyler** 09:23 Okay.
Let's see… we're 10 minutes in? I'm guessing Mike's not able to make it today, right?
**Ron Federman** 09:31 Light, I think… I think he might have a conflicting meeting.
Yeah.
**Tyler** 09:41 Oh, okay.
Yeah, sorry, I'm just looking at Slack right now. It looks like both Nicola and Mike, yeah. Okay, cool.
But yeah, cool, awesome. I think we could probably end it here. Nothing too much to talk about, we'll talk, but definitely some more, tomorrow's EB, or the OB meeting, so, yeah.
Well, cool, I'm looking forward to seeing you in… not next week, I guess, but the week after that, Ron. So yeah, pretty excited.
**Ron Federman** 10:07 Yeah, it's very soon, like, in 2 weeks, right? Less than 2 weeks.
**Tyler** 10:12 Yeah, as a person giving a talk, let me tell you, I feel it, so, yeah.
All that stress, but… Well, cool. Awesome. Alright, I'll talk to you next… I guess we don't have a meeting next week, so yeah, I'll talk to you, at Coupon, actually, yeah.
**Ron Federman** 10:27 Yeah, see you there.
**Tyler** 10:29 Bye. Yeah, bye.
