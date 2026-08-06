SIG: Collector SIG (NA)
Date: 2026-08-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 04:19 Should we start?
**Evan Bradley** 04:26 Let's do it.
**Pablo Baeyens** 04:28 Okay, I don't know that we have much… high priority things, the… the Kubernetes attributes PR, From last week, it's still open.
And it's the last piece before moving it to 1.0.
And… Yeah, I don't know. For the Host Manager Zero, there's been a bunch of work happening, but it's mostly on the semantic convention side.
So, I guess I'll jump to… my topic here.
just adjacent to this. So, I have a PR for, adding a configuration file for mDataGen.
Right now, it would be used for just the… sort of, like, skipping some linting that mdataGen does.
But, I want to also use it in the future for… Things like code coverage targets per component, which is something that it's kind of hard to do right now, and I would want it to be, like, if you're a… stable component, or a better component, you can have, A higher target than if you're alpha, for coverage.
So… Yeah, we want reviews, but I guess it's also a departure from how DataGen works right now, so I want general opinions about whether this is a good idea or not.
Because I could also do this just on each metadata or YAML files, but… I think this is a bit less annoying to do.
**Tyler Helmuth** 06:38 What does the scope look like? Like, is it like… when you run the command, whenever you use mdataGen, you run a command and you pass in… The config file for that particular run.
Datagen.
**Pablo Baeyens** 06:53 There would be an mdata gen config file for the whole repo, and the implementation on that PR is just it tries and finds it. It goes up the folders until.
**Tyler Helmuth** 07:04 Oh, okay, they're like,
**Pablo Baeyens** 07:05 button.
Like, the Golan CI…
**Tyler Helmuth** 07:08 Chart testing, a chat, yeah, CI, okay, yeah, yeah. So anytime you ran the command within the context of the repo, it would find that file.
Apply it, okay.
That seems generally useful.
**Jade Guiton** 07:26 Yeah, I would suggest having a way to explicitly set the path to the… To that file, but, yeah.
I think generally having that as the default is good.
**Pablo Baeyens** 07:42 Okay, yeah, so then, if you're gonna be, Feel free to leave that comment, Shad, and I'll… I'll…
**Tyler Helmuth** 07:53 For… I'm looking at the PR. For the example of, like, strict validation, If the top-level repo says skip strict validation false, I assume individual components are allowed to overwrite that and set it to true?
**Pablo Baeyens** 08:15 So my idea was that… also, no, like, it would be handled through the central configuration file,
**Tyler Helmuth** 08:27 Don't we have a bunch of things in Contrib that are… Like, I thought we added that field specifically because there are feature gates in contribib that don't meet our naming convention.
**Jade Guiton** 08:38 Things,
**Pablo Baeyens** 08:38 Yeah, so the first time we… Sorry, go ahead, Chad.
**Jade Guiton** 08:42 Yeah, I think what you might be missing is that the centralized file has individual options for each component in the repo.
**Tyler Helmuth** 08:50 Oh, okay.
**Pablo Baeyens** 08:52 Yeah, so you would be able to… to add those.
skipping, things that we have right now onto the central file. And I like that more because that way.
like, it's not code owners that handle this, it's, like, we have some sort of central place where maintainers handle this. It's similar to, like, Golang Sea Island YAML.
We can have a different code owner for this, and such.
**Tyler Helmuth** 09:21 I think that makes maintenance easier. One thing, I guess, to consider is that, The definition for how a component generates is no longer isolated just to itself. So, like, if I went and looked at a particular receiver, and I looked at its… at metadata.yaml, and I wanted to find, like, the metadata about it, I couldn't only look in the metadata.yaml anymore. I would have to look at its Addits file, and then also the top-level file.
So it does spread out a bit of the component definition.
**Pablo Baeyens** 09:59 Yeah, yeah, for the… the lifecycle test, for example, yeah.
Yeah, I mean, ideally, Node Component uses these skip rules at some point. Aspirational.
**Tyler Helmuth** 10:12 Yeah.
**Jade Guiton** 10:16 What would be the criterion for choosing which options are in the… per component files versus centralized? Because to me, it's not really clear What this changes besides maintenance burden?
**Pablo Baeyens** 10:32 So, right now, I put all the things that are, like, skip something that… ideally, you shouldn't skip into the central file, and then I would want to put rules that are not specific to components, but that are specific to maybe a component stability level. So things like the target coverage.
Or some other kind of test that we only want to require for… Alpha components, or beta components.
**Jade Guiton** 11:02 I see.
This new file wouldn't be required, right?
**Pablo Baeyens** 11:09 Not for now.
But my intention was to make it required at some point.
But… I guess that's a separate discussion, if we…
**Tyler Helmuth** 11:20 Excuse me.
**Pablo Baeyens** 11:21 Nobody will…
**Jade Guiton** 11:23 Yeah, I'm a bit concerned about that, because my assumption is that mDataGen is supposed to be used by basically everyone who wants to build a Collector component, and not just people who want it to live in Collector Contrib.
So, you know, If we have features that make maintenance easier for us, that's a decision on us, but… I feel like we shouldn't impose that, necessarily.
**Pablo Baeyens** 11:52 I think the way the PR stands… We don't necessarily have to make it required, I would like to make it required, but I guess, for now, I would like to focus on, like, is this a good idea in the first place? Required or not?
**Jade Guiton** 12:09 Yeah, makes sense. Although, what is your rationale for making it mandatory?
**Pablo Baeyens** 12:17 I… I don't know, I see a feature where we have some sort of… Well, it's not necessarily required, but we have some sort of, like, recommendations for stability levels, and everybody follows it, not just Contrib or Core, and so, like.
maybe we have, like, an ndata gen init config, subcommand, and, like, that's the first thing you do on your repo, and it sets the… the requirements. I don't know.
I don't feel too strongly about it, and I haven't… Thought about that future too much, because it's far away.
**Jade Guiton** 12:57 Hmm, okay, I see.
**Pablo Baeyens** 13:05 Okay, I think I… got the discussion I wanted, just… maybe leave a review in the PR, if you're… Interested.
And then I had one brief thing, which is I… filed a bunch of PRs to avoid using embedded fields in config structs.
Because, well, we've had a bunch of problems in that, It was maybe a bit more difficult before, but just… Quick.
some AI-written script, it was… easier to… remove those, and I want to introduce a rule on… a check on CI, basically, to avoid using embedded fields on config. So, I guess this is just, like.
Well, I have a PR for that, that it was merged but not released, so if you disagree with adding this as a requirement on CI, there's still time to… to let me know. But the main ask is, don't add new embedded fields on config, Until… I've got it.ca coin, if you can remember.
Because it's a pain.
So I drove them.
And I'll put a link to the PR… with the implementation…
**Tyler Helmuth** 14:32 Pablo, can you add a link to a PR that undid the embedded undid and embedded config.
As well. I want to see what our alternative was.
**Pablo Baeyens** 14:47 The PR that removed embedded fields and made them…
**Tyler Helmuth** 14:50 Yeah, did you say you already… you already merged a PR that removed embedded fields?
**Pablo Baeyens** 14:56 Yes, yeah, it's actually a few PRs, let me… Sure.
I think the best place to see that is… Yeah, so if you go to… the latest release, and you look at the API change log, they're… The links are there for…
**Tyler Helmuth** 15:31 Okay.
**Pablo Baeyens** 15:31 4, 5, 6, 7, 8, 9 PRs.
**Tyler Helmuth** 15:35 Does this have… Actually, I guess… Because of squash. This doesn't have any end user impact. This is just a change.
**Pablo Baeyens** 15:43 No, this is entirely false.
**Tyler Helmuth** 15:44 Stuck.
**Pablo Baeyens** 15:45 Yup.
**Tyler Helmuth** 15:45 Yeah, yeah, okay, cool.
**Pablo Baeyens** 15:48 Yo.
That's why I was a bit quicker on merging these.
Yeah, so… Thanks for doing your part on removing embedded fields, and that's all from me.
**Ravishankar Gnanaprakasam** 16:07 I think my item is next, so it's just an FYI, like, there are two PRs, I think Ivan is here, so… one of them, I think you have reviewed, so if you have some bandwidth, maybe you can take a look. The other PR, I think anyone can take a look. It's a… small PR for, fix an option.
Yep.
**Evan Bradley** 16:34 Hey, thank you. I'll, I'll take a book at both of these, hopefully later today.
**Ravishankar Gnanaprakasam** 16:40 Good. Thanks, thanks again.
**Blake Rouse** 16:59 Alright, the next one.
So yeah, this is a… PR for, the Export Helper.
Inside the retry sender, If you turned on retry, it handled… the shutdown case, where if retry was on and it shut down, the events that were being sent at that time We're not lost.
But he didn't have that turned on.
And the events are being sent.
At that time, they were lost.
So, my question is… I don't know exactly why I was putting retry, I don't know if that was, like… We only want to retry because it's shut down, but it felt… in my… I hid it in some scenario tests for the Elasticsearch exporter.
And it seemed strange that during shutdown.
The events in the persistent queue were being dropped.
Just because the error was shut down.
So this changes it to basically have a shutdown sender, and removes it from the retry sender, and the shutdown sender is always registered there at the beginning.
And so, basically, it gets signaled upon shutdown, the exporter does, through exporter helper.
And… those events are not dropped, is all this change does. It's a pretty simple change.
But I just didn't know if the behavior… Of placing it in retry, was specific.
**Tyler Helmuth** 18:53 The Gutru's not here, and he would probably know the best.
it… based on your description, this sounds like… bug fix, and it probably wasn't intentional, but since Dimitri's not here, I'm not totally sure.
**Blake Rouse** 19:09 Okay.
I just want to bring awareness to it, I felt like it was a bug fix as well, but didn't know if there was some intentional behavior.
**Tyler Helmuth** 19:21 Yep, people will take a look. Dimitri will probably be interested, but he's on PTO for, like, another week or two. So this might not be the fastest, VR ever, but, thanks for opening it.
**Blake Rouse** 19:34 Sure, yeah, no problem.
**Jade Guiton** 19:39 Speaking of which, do we know if the fact that Like, data is dropped… during shutdown, instead of flushed, once it's in the retry loop. Do we know if that's intentional?
Cause it is a bit of a problem.
**Blake Rouse** 19:58 Say that again? So in the re… if you have retry on.
Retrial and failure sets are true, it's not a problem.
Like, this is handled properly.
But if you don't have retrial and failure on.
And you're in… and you hit shutdown. Any event that was being sent when the shutdown occurred, any event that was pulled out of the persistent queue to be sent to the exporter.
And if the context basically is canceled before the request is actually sent out, Then you lose that data.
**Jade Guiton** 20:32 Right. What I meant is another situation where you don't have the persistent queue.
My understanding is that explorers are usually expected to flush their buffers.
On shutdown, instead of dropping the data on the floor.
I think that's what's happening with the retry sender at the moment.
Your PR would fix it for the persistent queue, But not for the… Memory queue.
And I'm not sure that's intentional or not.
**Blake Rouse** 21:07 In my behavioral testing, I didn't hit the issue in my pers… in the memory queue.
But… That could have just been Baile.
By coincidence?
**Jade Guiton** 21:20 Yeah, maybe, did you test cases where, like.
The first export fails, then it enters the retry loop, and then it shuts down?
**Blake Rouse** 21:32 So… The issue here, the behavior happens, so if It works fine, actually.
As long as the endpoint that you're sending to doesn't error.
that's where the problem comes from, so that's where I really saw this. So, I forced Elasticsearch to I was mocking Elasticsearch, and I was forcing it to return an error, and when you force it to return an error, it, during the shutdown.
With… without retrial and failure, you lose the events.
**Jade Guiton** 22:10 Right.
**Blake Rouse** 22:11 But you shouldn't really lose the events, because they were never really sent.
And it was in the retry loop. Well, no, it was… it wasn't in the retry loop.
So I guess that's my question, truthfully. Like.
Maybe it's found… maybe it should stay how it is.
**Evan Bradley** 22:37 So if your mock backend returns success, this doesn't happen, but if it returns failure, it does, is what you're saying?
**Blake Rouse** 22:44 Correct.
**Evan Bradley** 22:47 That… seems intentional, because it's been sent, and if retry and failure is off… Then it shouldn't retry it, right?
Resist it, and then later retry it.
**Jade Guiton** 23:03 Like, we're talking about the situation where returant failure is on, right?
**Blake Rouse** 23:07 No, Retron failures off.
**Jade Guiton** 23:12 Wait, so where is the retry center relevant?
**Evan Bradley** 23:19 Well, no, it should be relevant, right?
it shouldn't retry it. Like, if it… if you return… if you receive a failure, then it shouldn't retry it.
**Jade Guiton** 23:29 If retry and failure is off, doesn't it bypass the retry center altogether?
**Evan Bradley** 23:43 I would think so.
But it sounds to me like what's happening is retry and failures off, the Collector… Starts to shut down, the persistent queue is… flushed, or is flushed to disk independently of this last payload, and regardless of whether the payload succeeds or fails, it shouldn't be put back in the queue and later retried.
**Blake Rouse** 24:12 Well, I think the… I think the thing here is it's doing exactly what you just described. On shutdown, it's flushing the queue, right? It's flushing it.
But the problem is, is that the endpoint is in a bad state.
And so, it shouldn't really flush.
What's already in the queue.
just because it's in a bad… you know what I'm saying? It's in a bad state, it should really stop. Even with re… even without retrial and failure on, is my take on it. Because… you haven't even tried those events yet, right? Those are future events.
that are gonna happen, but you're hitting shutdown, so that you're gonna do a flush, but your endpoint is having a, a problem. So shouldn't we… Just shut down and leave them there.
That way, hopefully, when it comes back, the endpoint's back up, or we just want to say, on shutdown, we flush everything without retry and failure, you just lose everything on shutdown.
**Jade Guiton** 25:10 I mean, if the endpoint is down, and you don't have requirement failure, And… There's an attempt to send the data.
And it's just gonna drop the data on the floor, regardless of the persistent queue, right?
**Blake Rouse** 25:24 I'm saying, to send all the data due to the ending flush. Does that make sense?
**Jade Guiton** 25:32 Is it fleshing the persistent queue?
Hmm.
I don't know.
**Ravishankar Gnanaprakasam** 25:39 Okay, is it, is it your…
**Blake Rouse** 25:42 Yeah, it is. It says, item dispatching flushing, it deletes the persistent… it's flushing the persistent queue.
Maybe that's the true bug. Maybe it shouldn't flush to the persistent queue.
**Evan Bradley** 25:54 flush to disk, or… I was thinking flush to disk, sorry, that's what I meant. I meant it was taking the persistent queue, writing it to disk, so you no longer have anything in memory, it's all on disk now. You mean that it's taking from the persistent queue and trying to send additional points?
**Blake Rouse** 26:11 For my behavior testing, I believe it was trying… I'd have to look at it again, but when I was doing it, my behavioral tests were observed, and I can actually point to the behavioral tests.
Let me put them here.
Behavioral tests are… Where I had to handle this case.
**Jade Guiton** 26:28 Yeah, if the… if the persistent queue is flushing on shutdown, which is to say, it's reading everything from the… from disk, and then trying to send it.
I do think that is incorrect behavior. Like, the whole point of flushing on shutdown is to avoid having things in memory, but if it's on disk already, why bother?
**Evan Bradley** 26:48 Or at a minimum, it should flush 2DISC, not flush the queue… But I don't think it…
**Jade Guiton** 26:53 flushes to disk. I think it's already on disk.
Like, it's never kept in memory, I don't think.
**Evan Bradley** 26:59 Right, right.
**Jade Guiton** 27:00 I'm a recaching of the persistent queue at the moment.
**Evan Bradley** 27:07 What's that? Okay. I'm just trying to… because, I mean, obviously it has to live in memory at some point, right?
Yeah, but as soon.
**Jade Guiton** 27:13 as it's… Because when it enters the persistent queue, it's written to disk.
and then acknowledged, and then just… it's gone from memory. It's re-read from disk when you want to take it out of the queue.
Which is very slow, but that's what's happening currently.
**Blake Rouse** 27:40 Yeah, let me come back to you on what it's doing. I'll confirm if… If it's flushing everything out of the persistent key upon shutdown, that would be bad.
If it's not doing that, Then the behavior might be correct.
That… and that was probably the reason it was placed in retry and not a general shutdown.
**Jade Guiton** 28:07 Yeah, I'll… Take a peek at your PR, because I'm kind of… Interested to understand how this works now, but… I think… It'd be better to wait till Dimitri's back.
**Evan Bradley** 28:34 If you're able, while you're looking into this, the fact that we can't… well, I mean, obviously, I guess I haven't looked on this call, but if we aren't able to answer this question from the existing test suite and the exporter helper, that might be, useful if you're able to extract some of your behavioral tests into… Like, integration tests with the exporter helper.
**Blake Rouse** 28:59 Okay, yeah, I can look at that. I'll look at the integration tests around it.
Around Iceport Helper in C.
Yeah, maybe it's explaining it there, too, but I couldn't find it.
**Evan Bradley** 29:14 Either way, thanks for digging into this.
**Blake Rouse** 29:16 Yeah, I'll dig into it more.
**Evan Bradley** 29:30 That's all we have on the agenda. Anybody else have any items that they want to discuss?
Going once, going twice… Alright?
See everyone next time.
**Pablo Baeyens** 29:52 Dude.
**Jade Guiton** 29:53 Everyone?
**Ravishankar Gnanaprakasam** 29:54 reliable.
**Blake Rouse** 29:55 Right.
