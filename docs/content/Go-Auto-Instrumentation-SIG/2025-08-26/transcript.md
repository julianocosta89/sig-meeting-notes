SIG: Go Auto-Instrumentation SIG
Date: 2025-08-26
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 01:02 Hey, Tyler!
**Tyler Yahn** 01:04 Hey, Raphael, how's it going?
**Rafael Roquetto** 01:06 Good, how are you?
**Tyler Yahn** 01:08 Good, yeah, ….
**Rafael Roquetto** 01:10 be busy. I want Nika to come back.
**Tyler Yahn** 01:14 It's been… sorry, what was that?
**Rafael Roquetto** 01:16 It's been busy.
**Tyler Yahn** 01:17 Oh, yeah.
Yeah, it's, … Just, like, in… in the company, you mean, or just, hotel stuff?
**Rafael Roquetto** 01:24 Yeah, not in the company, and….
**Tyler Yahn** 01:26 Yeah.
**Rafael Roquetto** 01:27 People, like…
Took time off, and then at the same time, bugs decide to rain, and requests, and… so, perfect timing.
**Tyler Yahn** 01:37 Yeah, yeah, yeah. I kind of had the opposite problem, where, like, I got, like, some inspiration to go address some things, and all of a sudden I had, like, 15 PRs sitting there and no one to review them, so…
Yeah, it's, … yeah, it's definitely… it's that time of year where everyone's just taking it off, so it's like, I don't know, like, I forget about it every year. Like, every year, I'm always surprised when it happens, but it happens every year, yeah.
**Rafael Roquetto** 02:02 Yeah, it's been… it's been interesting. Lisa, I've been…
learning it, because, you know, there's no other way, so… super lining.
**Tyler Yahn** 02:11 Yeah, right? That's always a good way to look at it, yeah.
Hey, Mike.
**Mike Dame** 02:16 Hey guys, how's it going?
**Tyler Yahn** 02:18 Doing well, how are you?
**Mike Dame** 02:20 I'm good, thanks.
**Tyler Yahn** 02:22 Nice. …
I saw Ron said that he's not gonna be able to make it today, so… actually, we could probably just get started. I don't have too much on the agenda, so if y'all had, things you want to talk about, please go ahead and add them there, and then, you know, let's, ….
**Rafael Roquetto** 02:40 Yeah, you already did. Yeah.
**Tyler Yahn** 02:42 Okay.
Yeah, so I… yeah, I'm happy you're here. I wanted to just ask some, like, clarifying questions on this one, so…
I mean, I think it looks good, it's just, … You said that you would…
this is the thing I was kinda… yeah, so…
So it's difficult to ditch the explicit reference to the Clang 19, so this is where you were trying to update the configuration to be, like, more generic across every formatter?
**Rafael Roquetto** 03:09 Yes. So, for instance, if you format this with client 20, and…
… I'm trying to remember from the top of my mind. When you have a pointer to a function.
And… Sometimes we'll add a space, like, it's not aligning the pointer correctly.
Inside a macrobe, so it's a very specific case.
**Tyler Yahn** 03:36 Hmm.
**Rafael Roquetto** 03:36 And plane 19 has a different behavior than plane 20.
cling from it. And, I thought, okay, maybe because it's implicit behavior, I can try to make it explicit and force it, no matter the version.
But it doesn't work. Actually, there's no setting to do that. And I remember having tried that in the past now, because this is not a new problem, and the conclusion was the same, but I thought, you know, let me give it another…
shot, and then I started looking at the, you know, LLVM issues, and, like, Crawling the internet.
And apparently, it's really, like, a bug, and I don't think there is any way… like, the advice is, if you really want a consistent behavior, you gotta settle on a plank from aversion, which is very unfortunate, in my opinion.
**Tyler Yahn** 04:26 Yeah, … Yeah, agreed.
I think that's kind of frustrating, but…
But yeah, so I think that that kind of, like, brought me back to that point, though, then, is, like, we need to make sure we have some, like, consistent tooling to make sure that all developers are gonna use this… this Clang format.
Is kind of the idea.
**Rafael Roquetto** 04:45 Mmm.
**Tyler Yahn** 04:46 And so, did we want to look into Dockerizing, the makefile, or some sort of way to, like, …
I don't know, set it up so that that's always gonna be the case?
**Rafael Roquetto** 04:59 Yeah, I think that's, … That's a good idea. I can look into it in, like…
I'm thinking out loud here, haven't thought of it, but… Maybe we can…
have a Docker fight. It would be nice if there was some sort of, like, static
compile version of playing Format19 that we could just pull like we do with the Go tooling, you know, go to install, and that would be the best. I'll see if I can find something like that. I don't think there is, maybe I'm wrong, and nothing prevents us from building in any way. …
So…
That would be the best… I guess that would be the best, in my opinion, approach, because then there's no doctor involved, it's just like regular tooling the, you know, make and
pull it from somewhere and… and… and run it. Otherwise, we can look into seeing, like, as a fallback approach.
If this doesn't work.
If the user has platform and installed, I can try to guess the version, and if it's 19, you will run that, if it's not 19,
we fall back to a Docker image, for instance, I don't know, something like that.
What do you think?
**Tyler Yahn** 06:16 Yeah, …
So I don't, … I definitely don't want to be a distributor of, like, the Clang19 binary. That's not… I don't think we want to do that.
**Rafael Roquetto** 06:26 me.
**Tyler Yahn** 06:27 I do think that if you can pull it from somewhere, that makes sense, but if you can pull it from somewhere, I'm, like…
you essentially are recreating a package manager at that point. So, you know, I'm okay, like, if we wanted to try to, like, update this to, like, hook into popular, …
Like, package managers for, for, like, common developer environments, … I think that's gonna be…
… if we do that, like, we actually probably want to restructure a lot of this, because there's a lot of things in the makefile that, like, kind of just assume things are installed for you. In fact, we have documentation on, like, what tooling you should already have installed.
So we could… if, like, I'm not opposed to what you just said, like, if we wanted to do that, we could, like, set up, like, a script for…
you know, a Mac environment, or a Boots environment, or Arch Linux, or something like that. Like, all of these different environments that you could think of.
I think that's quite a project.
**Rafael Roquetto** 07:25 Yeah.
Yeah, yeah.
**Tyler Yahn** 07:29 I'm not opposed, like, I actually really like those projects, I've definitely, like, come into those and just been like, make, set me up, and it, like, does all the things for you, which is great. But I think that since we already have this Docker setup right here… Okay. Yeah, like, I think what you could do is you could say, like, …
I think… I think having this… …
leaving this target as it is, and just to kind of, like, hey, if the user's got Clang format set up, document somewhere, like, document in our contributing guidelines that Clang Format 19 is what we use. We don't, like, support any of the other ones, so, like, if there's any confusion, we can point to that. But then I would also add another target.
And that other target would be, like, … I think we call them, like, a prefix or a suffix.
of, like, docker-clink format. Sorry, I'm looking….
**Rafael Roquetto** 08:18 Right.
**Tyler Yahn** 08:19 Or, I can't remember if… I can't remember if… yeah. Yeah, so yeah, like….
**Rafael Roquetto** 08:22 I get the idea, yeah.
**Tyler Yahn** 08:24 Yeah, yeah, yeah. So, exactly. And then that one, it would just run with Docker, so if somebody doesn't want to install it locally, they could just use that target instead.
… I guess the hooks become a little bit harder?
But I guess if you're installing a pre-commit hook, like.
Maybe just also in the contributing guidelines, just say, like, hey.
it's… you need to have installed claim format if you want the commit hooks to work, I guess is what you say. Right. And so, like, that might be the way to go.
The… yeah, cause, like, the worry I have is, like.
we're gonna have developers, and I think we might already be in the situation, that work on projects that use a different form… like, version of Clank format, right?
**Rafael Roquetto** 09:02 Yeah.
**Tyler Yahn** 09:02 And so then they're gonna be really, frustrated when they're, like, coming to this project, it's one, and coming to another project, it's another. So if you could just, like.
forget that, and, like, just use, like, some sort of, like, standardized, like, environment with Docker, I think that'd be ideal.
….
**Rafael Roquetto** 09:19 Right.
**Tyler Yahn** 09:20 I do think the Docker one may not be that easy, though. … I don't know if there's a Docker image that already has this, yeah.
This might be… Yeah… So, I mean, there's, like, these third-party, like, Docker images, I guess.
maybe look at… I'm always a little bit sketched out about this kind of stuff, but…
But what we could also do is we could have, like, a local Docker image that's just a Dockerfile definition, and so we could go through that process as well. Essentially, some way to have the renovate bot maintain this is kind of the key.
**Rafael Roquetto** 09:55 Okay, okay. Yeah, I can… I'll look into that. I can't promise I'll have the time to do it until the next meeting, but I'll definitely… I'll try… I'll try to squeeze it in, it's just… it's been a bit.
**Tyler Yahn** 10:07 No, I….
**Rafael Roquetto** 10:07 I'll look into that.
**Tyler Yahn** 10:09 I got next to me.
**Rafael Roquetto** 10:10 The next one, yeah.
**Tyler Yahn** 10:12 It's not a top priority, so I… I appreciate you looking at it, but also, like, I wouldn't lose sleep over it, is what I would say.
**Rafael Roquetto** 10:18 Yeah. No, but, okay, alright. So, yeah, I quickly took a look also at the images, these third-party images, and no bueno. So, … yeah, I'll look into it.
**Tyler Yahn** 10:31 Yeah, and so what I would do there is that, like, you can then just have, like, a…
like, another target that's, like, a build target, and that build… that would just build, like, our…
you know, generic Docker setup, essentially, and then you can have a dependency on the Docker Clang format to say, like, you had to have done the build first, ….
But… Yeah, I guess…
Anyways, yeah, I think that's probably the way to do it. I think the Docker caching would work pretty well on that one, too, as well, so….
**Rafael Roquetto** 11:00 Okay.
**Tyler Yahn** 11:01 Yeah, just don't try to copy the entire directory structure into the Docker image, because that'll, cause a lot of clash. But anyways, if that doesn't make sense to you, don't worry about it, yeah.
**Rafael Roquetto** 11:14 Okay, okay, if I have questions, I'll bug you on Slack.
**Tyler Yahn** 11:17 Yeah, okay, absolutely, sounds good. Happy to help.
**Rafael Roquetto** 11:20 Cope.
**Tyler Yahn** 11:22 Okay, cool. With that, maybe just look at the rest of the open PRs. I think there's only one other one that is, yeah, this needs just an update. There's this require rule, for TestifyLint that still needs review. I had taken a look at this before. I think this is pretty close.
… Maybe we could just take a look really quick here.
Pending. Oh, okay, I haven't submitted this. Yeah, okay, okay, it looks like I was halfway through another review. …
Yeah, so I think this just needs more eyes on it, …
Yeah, okay. I don't know why I haven't submitted this yet, but maybe I haven't finished it.
Anyways… Other than that, I don't think there's anything else outstanding.
… cool, then let's take a look at the milestone. So this is the next milestone. I'm pretty heads down in trying to get the hotel upstream milestone done. Of course…
just… there's… there's a plenty to draw a line in the sand, because, like, Santa Convention just released 137, so we're trying to, like, include that as well, but hopefully this week we'll get Upstream's, release out.
When that happens, I think this becomes a little bit easier to try to get, our release out. I would like to, you know, there's a few things that we were already depending on, like a commit hash for the, …
the auto-detect package and that kind of stuff, so I think once that happens, we can try to maybe move this forward and be a little bit more, …
You know, harsh on what we want to cut from this release.
But I do think that this upgrade to 137 semantic conventions is important. If we don't do this, we probably should upgrade to 136, which is already in upstream.
But I want to keep this in here. This should get, the blocking issue right now should get removed within the next day. This is something waiting on upstream.
Obviously the Clang format, we just talked about that. I think this is a great one, we're really close on this, so let's try to get this in. Ron is working on this, I haven't seen any progress on this. I'm working on this, I haven't seen any progress on this either.
**Rafael Roquetto** 13:28 Well, okay, that's not true. I've seen progress, but it's been really bad, and it's local, and I haven't pushed anything, so I'm still working on this, and I'm guessing Ron's also still looking at this, so….
**Tyler Yahn** 13:39 Yeah, I think that… I think that if this needs to get cut into the next, …
release, that's not a problem. Similar here, I don't think there's anything blocking this. I'd like to get this in, just because, Rafael, you've done a lot of work on this, and it's already, like, 90% of the way there, so, yeah, I think we're gonna try to keep that.
**Rafael Roquetto** 13:56 Yep.
**Tyler Yahn** 13:57 Cool.
Alright, well then, other than that, I think the only thing blocking this is just the upstream release of this 137, so I think hopefully within this next week, we'll get another release out, is kind of my plan. There's gonna be a lot.
I think after that, we definitely have some, like, cleanup. The 123 Go version is probably gonna get dropped at that point, so…
Actually, that's a good point, like, where are we at on that?
a lot of, Go teams are dropping this, and upstream as well, dependencies. Yeah, so it looks like…
We probably need to maybe update our…
CI to start working with Go 125.
If we haven't yet… sorry, I'm…
if we have… this is something I missed, or, forgot.
I think it's here… Yeah.
Okay, so we probably need to start, testing with GO125 as well, to increase our capacity for… oh.
Well, we kind of already are. …
That kind of works out really well.
I like this rolling release thing where we just see stable and old stable. Anyways, okay, it looks like we're pretty far on supporting 125, so we just need to… can I get this next release out, and then declare that it's the last one, that 123 is gonna be supported for building and development, not for, instrumented packages, just to be clear.
Okay.
Cool. Any other things people wanted to talk about at that milestone?
I think that that's… about it, but I'd love feedback if you think we're missing something.
Otherwise, I can stop sharing my screen.
Any other topics people want to talk about?
**Rafael Roquetto** 15:57 I'm good.
**Tyler Yahn** 15:58 I know the maintainer meeting, or the maintainer summit at KubeCon this year is starting to get some, … I don't know if they've got… I don't know if they have the schedule announced yet, but I think it's coming out soon, so…
just a call for… if you are coming to KubeCon, or if you're listening to this recording and you're coming to KubeCon, you should try to sign up for that. I was told…
Yesterday, somebody asked me, I think if you're not, like, a maintainer, but you're active in this project, if you're active in this project, I'd love to see there, and if…
Not being a maintainer is blocking you from coming to that.
I think there's a way you can get, like, sponsored by a maintainer? So… yes, I'm all about you reaching out to me, or one of the other…
maintainers here to get sponsored there, because I think that, like, the more people we can get, there, I'd appreciate that. So, if that's just blocking you from coming to the Maintainer Summit, just reach out to me in Slack.
I'm happy to… happy to help there.
Although, I'm not 100% sure if, like, my sponsorship actually means anything, I just, yeah.
In theory, I think it… from based on what I read, yeah.
Well, cool.
Yeah, if there's nothing else, we can end the meeting early here.
Thanks, everyone, for joining, appreciate your time. We'll hopefully get another release out, and I'll likely see y'all tomorrow morning.
**Rafael Roquetto** 17:23 See you then. Bye.
