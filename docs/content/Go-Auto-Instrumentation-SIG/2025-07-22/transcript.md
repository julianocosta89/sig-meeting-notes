SIG: Go Auto-Instrumentation SIG
Date: 2025-07-22
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:50 Hey, Ron.
**Rafael Roquetto** 00:56 Hey, guys, how's this going.
**Tyler Yahn** 00:57 Going? Well, how are you.
**Rafael Roquetto** 00:59 Good thanks.
Nicola might be late if he comes at all. He got stuck into a different call.
So just letting you guys know.
**Tyler Yahn** 01:09 Okay, yeah, no worries.
Ron. Do you know, if Mike's able to make it today.
**Ron Federman** 01:20 And not true. Thank you.
**Tyler Yahn** 02:12 Yeah. So I mean, the agenda today is pretty light. I've only added a few things just kinda to check in on some things.
But yeah, if any of you have some topics you wanted to discuss.
please go ahead and add them.
And then we could probably just get started here. Actually.
yeah, I see, Mike's on. So
yeah, maybe we could just jump in all right. So
without anything to talk about. Prior to this, I just wanted to do pretty much our standard review. I don't think there's too much that's actually happened in the past week, so this should be pretty quick.
open prs, this.
add cross platform, perf reader, implementation and fix type mismatch. I think this is one where we've kind of given up on the original author trying to
over
all the missing functionality we wanted to do. Ron, you were saying that you were to look at doing this in the future. I'm guessing. This is still just something in the backlog that you're planning on doing.
**Ron Federman** 03:15 And yeah, yeah, for sure, I think I need to open like an issue for this.
**Tyler Yahn** 03:22 Yeah, yeah, yeah, just an issue just to track what we're missing.
**Ron Federman** 03:26 Thanks.
**Tyler Yahn** 03:27 Yep.
and then we can close this cool shift. Probe lifecycle management from probe to manager. Mike, you were talking about this last time you were thinking of closing this.
**Mike Dame** 03:39 Yeah, you know, I think that we can probably actually close this. I think that the idea is still there. But, we we've got a lot of other stuff that we're doing kind of to get to this point first.st So when we get back to, you know, looking at areas like this, I'm happy to pick it up and kind of I think we learned a lot from this. And yeah, I have no problem closing this. Now, I think we've kind of
focused on different areas, for now.
**Tyler Yahn** 04:03 Okay, I will close this. Obviously the reopen button always exists. Right? So.
**Mike Dame** 04:09 Dude.
**Tyler Yahn** 04:12 Cool.
Okay? And then some tree add tests for trace, id and span id. I think this one was something that was on me.
yeah, it looks like, I think this is just needing more
review. Yeah, okay, so this is just missing reviews. Okay, so this is definitely something.
I think, yeah, looking for review on this so hopefully, I can remember to do this. I'll keep this open and I'll get a review on this one.
I think this is straightforward. I think all the tests are passing.
I think they fixed the error to be what
makes sense. This is pretty small. I don't know why this is held up. So I think it's just on me.
Okay. And then the last one is this.
actually, this might be ready to merge at this point, update and Nope, it's not okay.
Okay, cool. And then kind of just following up. Also from last week we had talked about these goals. I think that we've got a pretty good plan going forward. I think it pretty much everything kind of relies on this phase. One setup for the I think it's yeah the ob phase one.
I think the only other thing would be this binary object file tracking, which I think I saw Rafael. You had made a comment on this, or maybe it was in the ob repo. But I can't remember.
Yeah.
**Rafael Roquetto** 05:38 Was last week.
Area.
**Tyler Yahn** 05:40 So yeah, we're we're definitely looking at. If I if I understand you correctly, just trying to make a decision at this point.
**Rafael Roquetto** 05:48 Yeah. So for ob, I mean, we haven't been
discussing that internally. It's kind of stale but the status quo is is with the sub module. That's what I've been using.
And yeah, as I said in the comment.
it works like everything like we said last time picture point, we got a picture of poison.
It's a module, is the upside, in my opinion.
is that you can reason about it as you would reason about any git sub module as a dependency, and then, the Vendor Directory, or you know the vendor dependency, just
it just becomes a consequence of using the go tooling, meaning that if you wanna use ob as a dependency you need to include as a sub module, for instance. Now, this might not be
not not be feasible, for people who want want only want to do like go get
the usual go tooling instead of having to mess with bits of modules, so that would be the downside.
**Tyler Yahn** 06:57 So this doesn't work with. Go, get, and like go install, and that kind of thing.
**Rafael Roquetto** 07:01 No, no, because the way it works. So let's say, you wanna vendor ob if you do go get with ob is gonna end up with in your vendor director, or, you know, modules Directory.
and and then you you have the same problem that we'd be having.
Which is, how do we generate object files without writing into the mode? Right? So that that this, if you want to do that, then you need to use Obgn files the the previous approach with the sub module means that
you really, if you wanna vendor or have ob as a dependency, you need to have a get some module with Ob in there. Then, when you do like, make, generate, it goes into the sub module
and generates the files there as if you're building entry. Like the actual main project, it will be project. And then, when, when afterwards, when you do go MoD vendor, for instance, and and it copies the sub module into the vendor Directory because there is like a what is it called rewrite? Or I forgot
keyword.
Yeah. So that's how it works. So that that's that's it.
Basically.
**Tyler Yahn** 08:10 Yeah, alright, I.
Yeah, I'm I'm not particularly keen because my goal is, and like my end goal is to get, go, get to work.
**Rafael Roquetto** 08:19 Right.
**Tyler Yahn** 08:20 But I think this is a good alternative to writing like just scripting languages as well. So I think this is good to document here. But yeah.
**Rafael Roquetto** 08:29 Yeah, I mean.
like you said, if if they go, if if the goal is, go, get this. This is not going to work. But at least we know we know why we're not going to be using this right? So that's yeah, that's fair enough. Yeah.
**Tyler Yahn** 08:47 Okay, alright. Thanks for the update on this. I think
I think it's really kind of on on me at this point to look further into some of the solutions that I've proposed to try to get. Go, get to work, and and evaluate them.
In contrast to this, and see if we really want to try to solve this. But
yeah, I appreciate all the hard work on this one. Rafael. Yeah.
**Rafael Roquetto** 09:06 No worries. Let's just a bunch of comments.
**Tyler Yahn** 09:10 It's more than that.
okay, I think that was it. All the other ones we did go over last week for our goals. So a lot of these things are held up on this phase, one support. So yeah, I, Nicola, it sounds like he's not gonna be able to make it today. But it sounds like it's work in progress on this. So yeah, we'll have to keep tune. This is, I'm guessing something else we can talk about tomorrow at the Ob
group meeting as well. So
okay, like, I was saying, light agenda. Nothing too big. I can stop sharing my screen here. Any other topics people want to talk about that are on the agenda
late editions.
If not, we can end it early, definitely, a lot of work to do. So
I doubt I'm unique in that. So yeah, well, cool. Thanks everyone for joining. I appreciate all the the work, and we'll see you all in a week's time.
**Ron Federman** 10:19 Still there, but.
**Rafael Roquetto** 10:21 But.
