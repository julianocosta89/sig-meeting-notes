SIG: Go SIG
Date: 2026-04-16
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:14 Hey.
**Pellared** 00:17 Hello. I thought that I would be late, but I'm here.
How are you?
**Tyler** 00:23 Doing well, yeah. Just, just super busy.
How about y'all?
**Pellared** 00:30 Same, same.
**Damien Mathieu** 00:31 Good.
**Bryan Boreham** 00:36 Nope.
**Pellared** 00:38 Cool, Brian.
**Tyler** 00:50 Cool, yeah, sorry, I was cleaning up some things. Looks like… I don't know, I'm guessing this might be one, yeah, David's here.
Sam wasn't gonna be able to make it, so we're probably actually… alright, Quorum, unfortunately, I don't think we have anything on the agenda, so if you have things you wanted to talk about.
Topics or… or, new things that you're working on?
go ahead and add those as well. And if you haven't yet already added an attendee, yourself as an attendee, please go ahead and do that.
But yeah, otherwise, just pause here and wait for a second.
**Pellared** 01:32 any PRs that are missing reviews, because I'm flooded with notifications, so if there's anything, you just let me know. David, you are smart.
**David Ashpole** 01:45 You know, I… I'm, in the process of… I've just… I don't know, people have different opinions on, like, the co-pilot reviews, but… They're actually really useful.
**Pellared** 01:56 Exactly.
**David Ashpole** 01:57 just, like, ask for reviews all the time. So I'm… I'm.
**Tyler** 02:04 Oh, rubber.
**David Ashpole** 02:04 person, right?
**Tyler** 02:06 Didn't you have, like, a co-pilot, review improvement thing? Did that get merged?
**Pellared** 02:10 Yeah, I merged because I decided that even if you do have comments, I hope that there will be… it will be any… you'll see improvement, so if you have any other comments there, we can just improve the iterate with it. I think… I think even in my PRs, I think I saw little improvements in the comments that Copilot did. Maybe it's just an accident, you never know.
**Tyler** 02:33 Yeah, that's kind of the hard part about that one, is, like, it's a little tough to figure out, but… Yeah, I'm with David, I think they're really, You know, obviously sometimes they mess up, but so do humans, so… Cool, looks like David has plenty of PRs, so we can… we can jump in here in just a second. Let me go ahead and start sharing my screen. Robert, I know you also have some PRs around, like, attribute slice stuff, right?
Did those need to get some review in this as well?
**Pellared** 03:06 Yes, they will eat. I think… I think… I have found one bug, or maybe not myself, it was an AI who found a bug, you know, a side effect, but I just noticed that the same problem is the other places, so I created a bug from the truncation of strings for the current one. So this is an easy PR, and then for the exporting of slices.
I created, and I'm right now also finishing the truncation.
Of values inside slices.
The problem there will be that I do not… we do not have also the full logic for For… for bytes, or byte slices.
**Tyler** 03:44 Yeah, Robert, can you… can you grab the PR and maybe put it on the agenda, and then we can, talk about it?
**Pellared** 03:51 Yes, I want to do this.
Quickly.
**Tyler** 03:54 Okay.
I think to start us off, though, let's maybe jump in with, David's PRs here. He looks like, these are some runtime semantic conventions, so let's open these up. I'm guessing you're looking for a review on these, David, or do you want to talk a little bit more in depth?
**David Ashpole** 04:10 I just wanted to, like.
Give, give some of the rationale behind them, maybe discuss them as a group if other people are interested, because these are… So, First, I'm trying to stabilize the new runtime metrics, and as part of that, there's a couple metrics that are going away, right? So that were part of the previous set.
That are not part of the new set, and we've got some user feedback.
But… those metrics going away is gonna, like, negatively impact people. Like, they find them useful, in various scenarios. So, this is basically my attempt to address all of the outstanding feedback that we've gotten on the new runtime metrics.
And everything here is opt-in. So, I think the two… the… both of the memory GC ones are… I would say, kind of, Non-controversial, they're opt-in, They're, not… the Go maintainers strongly recommended using the schedule duration over the pause duration, which is why the schedule duration is on by default, and the pause duration is opt-in.
But I guess some people still find pause duration useful, so that's included here as something that could be turned on.
And then the other one is the GC count, which… Actually seems quite useful to me. It's only one cardinality, and We'll tell you if your garbage collector is running like crazy, which… yeah, it can be useful. So, I think this one is… I'm adding it as opt-in, but if others feel differently, we can consider making it on by default.
I think those are less… less interesting, maybe, for the group, and more of just, like.
FYI, and reviews are welcome.
**Pellared** 06:02 Regarding the BC one, is there anything… Other than that, that will tell you any other metrics that will tell you that you have the garbage collection key kind of frequently, which says that you're doing something wrong with, you know, key allocations and stuff like that.
**David Ashpole** 06:21 I would have to go look back at the original Go… like, the original issue from the Go maintainers. My recollection was that Go's schedule duration is, like.
Extremely useful at showing all Types of problems that make it so that your application isn't actually running.
The other thing that I'll cover in the CPU and memory one is that there is actually a CPU metric that breaks down how much time is spent in your user's program versus how much time is spent doing garbage collection or other things. So that… that metric is, like, maybe an alternative.
**Pellared** 06:55 Even in.
**David Ashpole** 06:55 to this GC-specific one.
Yep. Yeah.
**Tyler** 07:07 Cool, and then this last one, David?
**David Ashpole** 07:09 Yeah, yeah, so this… this is the most interesting one. It's got the biggest wall of text, as you can see as well, but… So, Josh McDonald has been asking for a while to have a… A metric that gives them access to the… Go CPU time breakdown, which, as I said, can be useful.
It's kind of misleading as well, because it doesn't line up with, like, what you'll get from your container stats, so leaving it maybe opt-in, so that people hopefully read the docs or something before they turn it on, seems potentially, like, a good idea. That's why it's still opt-in.
I think the most interesting part of the discussion is not whether to include a CPU metric as opt-in. That, to me, seems, like, perfectly reasonable.
I wanted to go over the way that the attributes are being split out here.
So… you'll notice that GoCPU time has two different attributes on it. One is GoCPU state, and one is GoCPU DetailedState.
And basically, what I'm trying to… and I'm using the same pattern for the memory metric as well, which is that… I'm trying to balance two things. One is that we'd like to give users Relatively… or we'd like to give users a stable High-level set of attributes.
That they can rely on for building dashboards.
But then there are going to be other users that really want to see the detailed breakdown that the Go Runtime gives them. Like, what are all the memory class categories, and what are all the CPU class categories that the Go Runtime reports?
And so, what I've opted to do is to have one Attribute, that's the high-level one that's likely to be stable.
And another one that basically takes everything under the classes and reports it as is.
And might change version to version.
And the first one is enabled by default, and the second one is opt-in.
The detailed state?
**Tyler** 09:17 Is opted?
**David Ashpole** 09:17 Detailed state is opt-in, and is of the form, like, stack slash other or something.
Brian?
**Bryan Boreham** 09:27 So I'm in favor of this information being available, I just, one, didn't get why the word classes got renamed to both type and state.
**David Ashpole** 09:43 It's a good… I mean, that's a reasonable question. Do you know where classes comes from? Like, as a user, I don't intuitively have a sense of, like.
What it's trying to tell me.
**Bryan Boreham** 09:56 I think the words… Type and class can be batted around by computer science.
**David Ashpole** 10:04 I see.
**Bryan Boreham** 10:05 I see.
**David Ashpole** 10:07 Like, go.memory.class.
**Bryan Boreham** 10:11 I mean, all of these, it kind of means category, or something like that, doesn't it? But I guess, yeah, so I have two questions, like, why change it at all, and why change it to two different things?
**David Ashpole** 10:24 Yeah, I can… That's good feedback. We can look at changing it.
I think… The original ones were modeled after some of the Java metrics that used memory.type.
And so there's… I think maybe something to be said for consistency there.
I wasn't sure… Class to class makes sense. I wasn't sure if it… Yeah, class can mean some things in other languages, maybe?
But… I'm also okay.
If we want to… naming's hard, right?
**Tyler** 11:07 Yeah, I mean, I think consistency's helpful here, but… I guess, like, if there is, like, precedence in the Ghost space, I'm also fine changing.
**David Ashpole** 11:18 I bet.
**Bryan Boreham** 11:19 And… sorry, I mean, probably the wrong rabbit hole, but just very briefly, the thing about what you should be looking at to understand, for instance, your garbage collection is the assist.
Particularly the assist time, because that's when it starts stealing time from what your program was trying to do.
But the sum of assistant dedicated should be the total time being spent on GC.
And… and so that might be the most interesting thing to care about.
**David Ashpole** 11:54 Okay, that's helpful feedback. If you're able to… leave that on the PR, I can try and integrate. I think… I believe I had a category here of just GC.
That was the… some of those, too, but I… we can double check.
If it's helpful to split out assist, even for the high-level one, then… We can change around the… Like, that… The high-level one, the goal is to have just 2 or 3 categories or something, that… Gives users enough information.
And that isn't susceptible. Like, one of the things that came up in the discussion with the Go maintainers was that they really want to have the ability to change these with new Go versions if they want.
And so… The recommendation was kind of, like.
For most users, can you please give them stuff, like.
that isn't likely to change as long as Go stays a memory-managed programming language, right?
So, like, categories like user and GC.
seemed safe. Scavenge, yeah, I don't… I didn't look too much time… or too much at scavenge, and idle seems also useful and likely to be relevant forever.
But…
**Bryan Boreham** 13:18 Yeah, I mean, it… Basically, the minute you get some indication that you have a GC problem, I go to the memory profile, so… Also, it's barely worth looking. You know, it's always memory allocation.
**David Ashpole** 13:37 Fair.
We'll just have an info metric. Is memory allocation the problem? It's always…
**Tyler** 13:48 It's always true.
Yep.
Okay, cool. So, yeah, I think, just to kind of close this out, you need some reviews on this. Brian, it sounds like it'd be great if you could put in some of your thoughts that we already talked about here, just to document them, if you can, and then other Go approvers also take a look, right?
**David Ashpole** 14:09 Yep.
**Tyler** 14:10 Cool.
Alright, David, also, allocations on the hot path for the, metrics POC?
**David Ashpole** 14:18 Don't… don't look at the code.
Just look at the PR description.
This… this is mostly, like, a question of whether it's possible. We had discussed a while back trying to use an unsafe version of the attributes function.
And, it lets us do a… A whole bunch of different optimizations, which… I had an AI do for me, so please don't look at the code.
But, this is just to show that, like, it is actually possible if we can get the raw attribute slice passed to the SDK to… You can look at the benchmarks, I think that's… The two interesting pieces of this are the benchmark results, which show that We have no allocations, even when we're doing filtering.
And that for most cases, we get, like, you know, from 2,000 nanoseconds to 166. Like, we get some pretty big performance improvements by doing this as well.
Compared to with attribute set.
I can… I'm happy to walk through the optimizations that are made here, or if… My plan is to start breaking this up into smaller… PRs. I'll probably start with just a very basic with unsafe attributes, without making some of the optimizations, and then go from there and Eventually, it'll be performant, presumably.
**Tyler** 15:55 So this is your… so the unsafe attributes are always gonna be… It's interesting, you're comparing unsafe attributes versus the attributes set.
Is that… Because attributes…
**David Ashpole** 16:06 set is more performant. Like, I could put with attributes on here, it would just always be.
**Tyler** 16:12 Okay, but the type signature with unsafe attributes is a slice of attributes being passed to them?
**David Ashpole** 16:17 Yes, yeah, you have to… it has to accept the slice.
**Tyler** 16:20 Yeah, no, that's fine. Yeah, I just wanted to make sure I understand.
This is gonna be a… experimental option, right?
**David Ashpole** 16:28 Yep.
The main thing that I would need while implementing this?
is, new functions in the attributes package.
For computing hashes.
So right now, you can't compute a distinct without computing a set.
And that turns out to be, like, important.
Initially, I was thinking we would be able to templatize it.
But I don't think that works, because we don't want to have a case where the SDK is on one version of the hash function, and the attributes package is on a different version.
And they don't compute the same hashes. So, I think the only way I can actually go forward with this is if I start adding Like, new, distinct, and… New distinct with filter.
type.
Type functions that takes a slice of key values.
**Tyler** 17:20 Yeah, honestly, that seems reasonable to me. I've always kind of thought that it was a little, like, We hide that away in the set, but we also, like, expose a distinct from the set, so it's like… It seemed like there was a missing functionality there, So, yeah, I mean, that seems reasonable to me.
I do wonder, though, in the long haul, though, David, like, so what… Are we ever gonna become confident enough with this unsafe attribute, like.
Function or option that we just say, okay, now we're gonna change out the width attribute, like.
Method to just be the unsafe attribute one?
**David Ashpole** 18:10 I think it… so, to be clear, like, the reason why it includes unsafe is because once you pass the slice to the function, you can't use it anymore, right? So… If you're constructing it like most people do, by just constructing some key values and putting them in, then it's fine. If people are… Taking that.
**Tyler** 18:31 Yes.
**David Ashpole** 18:32 slice and reusing it, then it's not safe, right? So part of it's, like.
How difficult do you think that actually is for users to get right and not shoot themselves in the foot?
I could see it being a replacement for with attributes set. The only issue here is that there is a regression compared to it.
In the pre-computed case with no filter, because With unsafe attributes does not compute the distinct.
And cache it in the option itself.
**Tyler** 19:08 Yeah, and like, the type signature doesn't match.
Like, the… this is getting past a set, this is getting past a slice, right?
**David Ashpole** 19:16 Yeah, but it's easy enough.
If you can make a set, then you can, like, right.
there would be work for users. I think it's… the other question in my mind is, like.
we wouldn't… We wouldn't want to add this if we were gonna… pursue, bound instruments, and it sounds like there are others who are gonna reopen that, discussion anyway. So, for now.
I'm more interested in this as a… an experimental thing.
And… I think it would be worth promoting to the stable API at some point, but Really, only if bound instruments didn't pan out.
The nice thing about this is that some of the… so some of the.
**Pellared** 20:03 I have another idea.
Maybe it's a little bit crazy and controversial. Have we thought about having some environment available Which will kind of, depending on… yeah, the default will be the same, that you'll copy the attribute slice, but you've opted in, then it will behave like unsafe.
And we could keep it for a long time, put a lot of warnings, etc.
Because I have no idea how otherwise we could, you know.
Maybe you can find out some other ways to, you know, just ask people.
Listen to… yeah.
**Tyler** 20:46 Well, I… I think… I think for experimentation, I kind of like David's approach here better. Like, putting it in an X package, and then adding an explicit option.
If you're talking about, like, long-term integration into, like, the main… Yeah, long-term. Yeah.
Yeah, I mean, I'm not… that seems… like an option.
**Pellared** 21:07 implementation, I agree, I think it's safer to have it explicit in code, especially that we have Sputter to have it separated already.
then, yeah.
**Tyler** 21:18 Yeah, as long as we name the environment variable spicy, I think then… I think we'll be all set.
Yeah, I don't… Yeah, Hotel Spicy, Hotel Go Spicy.
Yeah, I don't know, like, I think… I think maybe that's, like… too far ahead in the conversation.
But maybe, to your point, and, like, I was also kind of talking about that, so maybe it's just, like, if there is a path forward, I guess that's fine. Yeah, because, I mean, I guess the idea is, like, if we're just gonna do this, and then we're just gonna throw it away, that, like, we shouldn't do that, but I don't… I don't know. I think it… even leaving it as an experimental thing… Seems… seems fine.
At least for now. Yeah, that seems like… I think I'd want to pursue what David's got proposed here, I guess, is what I'm saying.
Including the distinct stuff, and then, you know, moving that forward. How that looks in the long haul, like, maybe… maybe that's… maybe that's something we just pause on and, like, ask, like, users of this, you know, what they think. Like, we can find people that are actually importing it and, like… say, like, hey, if we wanted to migrate this to the stable API, like, how would you like this to show up? You know, would it be, like, an environment flag you could turn on? Should we add it as its own option there? Should we just replace the attributes or something like that, yeah, so, I don't know.
I think that's maybe something we can talk about.
**David Ashpole** 22:43 I do think there is a path here still.
Where, if this were promoted to the public API, that we would consider deprecating, with attributes set.
In the… Pre-computed cases with attributes and with attributes that are identical.
Because, I mean… It just… one wraps the other, and if you only call it once and store it in a global variable or something, or a… But basically, like, the one case where you still need the… The old options, which is in the pre-computed cases.
It… it really doesn't make a difference whether you're using with attributes or with attributes set. So if we did want to deprecate with attribute set and attribute.set, the concept we could There is still a path towards that.
Eventually, maybe. But maybe that's also too far.
**Tyler** 23:39 I probably wouldn't want to deprecate the with attribute set, just because, like, it… it… Puts a worldview on, like, how you want to work with these attributes, and there may be users for working in the attribute set.
Type, especially since that thing itself, you can do filtering, you can do a lot of, like, higher level, Functionality on it.
I do think if we ever went to, like, a V2 on this kind of stuff, I think that'd be a great time to pull it out, but I don't know if I'd want to deprecate it, just because, like, I do think that there's, like, users that… Would want to use this.
**David Ashpole** 24:12 Okay, that's also fine. I think it sounds like people are okay if I start opening PRs with… With some of these experimental pieces, which is…
**Tyler** 24:24 Cool.
Cool. David, I think you also have the next, PR…
**David Ashpole** 24:33 Yeah, I was looking into some super ancient Regression memory issues, trying to figure out What was up with them?
And I realized that Even if you specify that there's basically no way to turn off.
memory usage. Not allocations, but memory usage from exemplar reservoirs.
So if you… If you set an always-off filter.
You still get your reservoir, you just get a filter in front of it that makes it never do anything.
So… Seems like…
**Tyler** 25:14 Dude.
**David Ashpole** 25:15 Yeah. Yeah.
**Tyler** 25:17 Okay.
**David Ashpole** 25:18 But Yeah, that… That's… so that's the issue, is that you're… When people upgraded to 1.30 or something of the metrics SDK and got exemplars enabled by default, their memory usage went up by something like 10x.
And they were confused.
Because it turns out the exemplar Reservoir is much, much larger than, like, a counter.
**Tyler** 25:46 And that's just, allocated memory, not necessarily, like, populated memory?
**David Ashpole** 25:54 Mmm… I wasn't able to look… It is allocated, for sure. I don't… Yeah, it never gets something put in it, for sure. So maybe it's possible that This is just, like, a measurement issue, and…
**Tyler** 26:11 Well, I mean, yeah, it's a measurement issue, but it's a real issue, right? Like, if you allocate to the GoSpace, like, you literally can't allocate it to something else, right? So, like, that's still a problem. I just, like… it's just whether that increases you know, churn because it's trying to access that memory or something like that, I think is kind of also, like.
**David Ashpole** 26:30 Yeah, it's never accessed. So, right now, if you have an always-off filter.
You get a reservoir created, but there's a filter in front of it that always returns false whenever someone calls.
**Tyler** 26:42 Hmm.
**David Ashpole** 26:43 on it. So the only thing I don't like, or the main problem I ran into is that always off Filter is a function.
And functions are not really comparable.
So, the spec says, like, Always off should function as disabling all exemplar-related behavior.
Should not being the normative, should… should just being… Which is probably why we didn't catch it. But, basically, the only way I could come up with to actually make this work is to use Reflect and do pointer comparisons. But I know that that's not…
**Tyler** 27:20 Can't you add a method to the function?
**David Ashpole** 27:23 I don't… It's not a, like… I mean, it's actually just a function, like…
**Tyler** 27:34 Yeah, but it's a declared function at the top level, right?
You should be able to add a method to that and just say, like, have it return, like, a static identifier.
I could… I could…
**David Ashpole** 27:55 Yeah, you can leave a comment. I tried to look into it, and I couldn't figure anything out. There was one option where we changed it to a variable.
and the variable points at a function, but that… I don't think that's backwards compatible.
**Tyler** 28:09 No, yeah, yeah.
Yeah, this is more like it would extend the function to have an additional thing that we could… I, I can… I've got an idea, but… Okay.
**David Ashpole** 28:19 Good, good, good.
**Tyler** 28:20 Yeah, we can take a look.
Oh, yeah.
Okay, I've got it open. I won't lose it.
But otherwise, yeah, I mean, I think at the bare minimum, what you're proposing here seems Like, a positive step forward, so that seems like a good idea, so yeah.
Yeah, that sounds good.
Awesome.
Okay, moving on, Robert, looks like you've got some of those PRs we were talking about. Pull those up.
**Pellared** 28:54 All of them are kind of quick, but at least we have We have time so we can discuss if anyone has any questions right now.
So, the previous one was adding, this, the instructions mainly for the co-pilot reviews.
This one, I hear I tried to make the agents MD, which is used by various AI agents. So, if you… I'm sure… I just put it as a draft.
I'm experimenting and trying to use this file right now, and I'm using different AI tools when creating my PR, so each of my PR, I try to write which, which AI tool I have been using. Still, it doesn't mean that this agent MD is really improving anything. For instance, I'm not sure if the default workflow really does anything.
for co-pilot, so I'm not even for planning, etc, so I'm not really sure.
Also, this may change in the future, what else? Yeah, but if you have any… any observations, or use cases, or recommendations, then feel free to give in comments right now.
Even before it's undrafted.
**Tyler** 30:07 So I definitely think, we need this. So that's, that's definitely my feedback. Because, like, especially for people that aren't familiar with all of these things you've included in here, like, new contributors to the project, this is, like, the way they're going to be contributing is through some sort of, like.
AI coding tool, and this will help, I think, improve the quality of what their PRs churn out. So, I… I think This looks… this looks good. I haven't looked, obviously, through all the details, but from what I've seen so far, like, I think this is… this is great.
**Pellared** 30:39 Okay.
**Tyler** 30:41 Yep. Cool.
I can take a further look later, though, for sure.
**Pellared** 30:51 This is a bug that I just discovered when implementing, limit… attribute limit… value limit for slices. So, this is just doing for string, and I also checked, So this was… Okay, I can up… Yes.
Is… Yeah.
**Tyler** 31:23 Is the… Is the… is the limit defined on characters, or is it defined on…
**Pellared** 31:29 characters. I put it in the… I put it in the description. It's explicitly defined on the characters in the specification.
**Tyler** 31:36 Yeah, I know we… And I literally have had this conversation which caused this, but okay.
I think I might have made this edit as well, but I couldn't remember what the decision was.
Okay, cool. Then yeah, that sounds great. Let's… .
**Pellared** 31:51 I will still double check it myself later.
**Tyler** 31:54 The reason…
**Pellared** 31:56 Okay.
**Tyler** 31:56 Is there any reason to not put this in, like, the as string?
Oh, no, okay. Because it's gonna… no, because…
**Pellared** 32:06 It's in the SDK. It's the SDK procedure.
**Tyler** 32:09 Okay.
Okay, yeah, that sounds good, this looks good.
Cool, moving on? Is that right?
**Pellared** 32:18 Yep.
**Tyler** 32:19 Okay.
**Pellared** 32:25 Here, I, also try to describe my experience using Codex with the agents, so, initially.
the code it created looked very good. I would not create it myself that good, but still, then later, asking a codecs to review and copilot, I still was able to improve it a little bit, but this was just, you know, like.
baby step improvements. So this is just adding, adding the support for exporters to handle size attributes.
**Tyler** 33:00 Cool, yeah.
**Pellared** 33:02 Yeah, the zip key, I, I just defined as best support support. I do not want to, I didn't… because it's deprecated.
And I remember that it was defined when I was reviewing your PR, it was defined that it should be JSON serializing, I didn't want to waste too much time.
For either given… yeah.
So that was my shortcut here.
**Tyler** 33:24 I think that sounds great.
But all the others, look, Pretty similar, right? Yeah.
For what, you know.
Cool, alright. Yeah, so just reviews on this, nothing else other than that, right?
**Pellared** 33:42 Yes.
**Tyler** 33:43 Okay.
And then, last one, I'm guessing this is maybe some limits?
**Pellared** 33:51 Yes, these are links.
And I'm still just double-checking it, it's mostly already. I'm just double-checking, triple-checking everything.
**Tyler** 34:02 I see, so it's just, you're giving it some reviews, it's not… is it ready for other people to take a look at, or.
**Pellared** 34:08 I think it will be ready in a few hours, in an hour or two.
**Tyler** 34:12 Okay, cool.
Ugh… Yeah.
**Pellared** 34:18 Functional heart.
**Tyler** 34:19 This is the hard one. Although, the good thing is, is once you get this, it's, it should be, pretty easy to do the map one as well, or similar to do the map one, right?
**Pellared** 34:29 That's correct.
**Tyler** 34:30 Yeah.
Okay.
Okay, cool. Yeah, yeah, so it looks like it's just we need some reviews on most.
**Pellared** 34:38 space.
**Tyler** 34:39 Actually.
**Pellared** 34:39 Maybe one comment for the draft one?
These patterns used for the truncation are, like, these are… this is kind of… taken from the code, which is an SDK of logs.
So these patterns were already there. I asked GenAI to, you know, reuse these patterns, because they're working, and I'm double-checking. Also, the things which is missing here, which I wanted to double-check.
are the benchmarks. I want to also run it with benchmarks.
I… if I remember correctly, there will be some HIPAA locations, because each time we are accessing a slice.
We are copying it.
But we are copying the slice, because everything is safe on the package. We do not have unsafe as swing slice, unsafe as slice, so each time we take something, I think it causes a key allocation.
But I think for now, I would keep it this way.
and move… and create performance improvements to decrease… to decrease the number of people allocations in a separate PR if we want. But, yeah, but I think… yeah, but first, benchmarks, anyway.
**Tyler** 35:53 Cool, alright. Yeah, sounds good.
Okay. Does not cover bite slides.
Is this being addressed in a different PR, I thought?
**Pellared** 36:05 Exactly. Yes, I didn't want to just, you know, do the same stuff, which is already the other… I can always… I will always… I will remember about it, even if it doesn't get addressed properly, you know, because… because of, you know, synchronization, we'll figure out later.
**Tyler** 36:23 Absolutely, absolutely.
Cool, alright, yeah, definitely looks like we need some reviews, all around.
So, I'll clear my schedule.
Cool. Awesome. So that's the end of the agenda. Any other topics people want to talk about?
**Bryan Boreham** 36:50 Can I just say it's really annoying that those limits are in characters, not bytes?
**Tyler** 36:56 Yeah.
**Bryan Boreham** 36:58 Like, slows everything down, trips everyone up.
It's not what anyone expects.
**Tyler** 37:05 Yeah. I mean, the upside is, though, is that you don't get partial Unicode values showing up in people's UIs, but yeah, from a developer experience, like, it's kind of annoying, yeah.
Yeah, I… I think you're kind of… I think the limits thing is always a tough one, too, because you're just, like, you're already playing with an error case. Like, you're already just, like.
in a losing game, I feel, but it's just a tough situation. Yeah.
Yeah, why can't everything just be infinite memory? Yeah.
Well, cool. Alright, if there's nothing else folks want to talk about, we can probably end the meeting early here. Thank you all for joining. It's good to see y'all. I will see you all in a week's time, or asynchronously. Till then.
