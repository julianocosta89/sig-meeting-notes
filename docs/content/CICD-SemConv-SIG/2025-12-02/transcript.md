SIG: CI/CD SemConv SIG
Date: 2025-12-02
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:58 Hello.
**Adriel Perkins** 01:00 Good day, how are you?
**Christophe Kamphaus** 01:03 Mine, and you.
**Adriel Perkins** 01:05 Doing okay, thank you. Doing okay.
We'll give folks a couple more minutes just to enter anything they want to enter, or hop on, since it's just me and you right now. I have a somewhat of a hard stop at around the half-hour mark.
But we might not have enough to talk about anyway, today, so…
**Christophe Kamphaus** 01:57 Yep.
While waiting just to say, next week I won't be able to join.
**Adriel Perkins** 02:05 Okay, cool, yeah. Appreciate the heads up, for sure.
**Christophe Kamphaus** 02:25 I guess we could already take a look at triage?
Not sure if there's anything new there.
**Adriel Perkins** 02:33 Yep, yep, sure thing.
Actually, let me see if I can do it this way.
Overall.
**Christophe Kamphaus** 02:54 No, I don't see anything new.
**Adriel Perkins** 02:58 No, me neither.
I didn't get to, work on… this last week, so I was just starting to… to do that.
**Christophe Kamphaus** 03:22 What we discussed some time ago, to create the issues on the board.
**Adriel Perkins** 03:27 Yes.
I'm just gonna make this kind of like… Kind of like an Epic, but… Basically, it's just gonna be an issue with sub-issues, and the sub-issues are gonna in their respective repositories. Yep.
And then that way we can view, like, the main containing issue is gonna exist on the specification repository, because that's where it's, like, originating from.
And then these sub-issues are going to be linked to the different SDK repositories, which should work.
I might have to do some finagled syncing, but it should work.
**Christophe Kamphaus** 04:12 Yeah, sounds good.
**Adriel Perkins** 04:29 Let's actually put this at December 16th.
And we'll end, we won't put an end date.
Let's see… Let me go back to the community page.
I don't remember which ones we… Outlined that we wanted to take… I don't… I know we did… we wanted to go… So our four primary ones were Python, Go, C Sharp, JavaScript, but we should be able to do pretty much all of them, I think.
But those were our main target ones.
And I'm actually gonna add an action item to the board.
For next week.
Basically any… there… there might be some other things, like, I think the… There might be a couple things that we want to just take a look at, Porting over from the actual community document into our board, so that it's, like, tracked effectively.
So that's the action item that I'm adding here. So let's see, if I could spell update, or propagation… Rob, patient.
Alright, so… It would not be GO, it would be… yeah, it would not be GO Contrib.
And…
**Christophe Kamphaus** 08:34 So, basically, it's implementing the spec.
That you updated.
Some time ago, these two.
**Adriel Perkins** 08:55 see, what else did we call out? C-sharp, JavaScript.
Jack here.
**Christophe Kamphaus** 09:04 suspense.
only JavaScript missing here on the list from what we put on the… Phase 2 project, community.
H.
**Adriel Perkins** 09:19 But the others as well.
in here.
I'm not sure if it's the API, or… I think it's just JS.
But… Let's do Ruby. Ruby's a language we have.
Do people use Ruby? I don't know.
I assume so.
Do you have a C++ CPP? Yeah, we do.
**Christophe Kamphaus** 09:54 Yep.
Nonsense.
OpenTelemetry Java, OpenTelemetry Android, OpenTelemetry Swift.
**Adriel Perkins** 10:05 Oh yeah, that's right.
forgot about Swift.
Do you think Android would be… Do you think we'd want to do Android?
**Christophe Kamphaus** 10:18 No, I guess it doesn't make much sense, because… We are really for launching other processes, and on mobile, that's not really…
**Adriel Perkins** 10:27 Oh, it's interesting, too.
**Christophe Kamphaus** 10:30 There's PH… okay, you have PHPs there.
It says, heirloom…
**Adriel Perkins** 10:56 Is there an Erlang?
**Christophe Kamphaus** 10:58 Yes? Nice.
Oh, it says a Rust one.
**Adriel Perkins** 11:09 Oh yeah, I can't forget Russ.
That'd be great for Rust. People write… definitely write CLI utilities in Rust.
Is there… what other? Am I missing a language?
We have so many languages. Oh, I know where to find out what other ones we might be missing. Let's see… language and SDK. So C++.net, Erlang, slash elixir.
Go, Java, JavaScript, PHP, Python, Ruby, Rust, Swift.
And then there are 3 other languages, but it looks like there is no SIGs around them, so… The other languages are Lua, Pearl, and Julia.
But I don't… I don't think they exist, so… Yeah.
**Christophe Kamphaus** 12:18 And that should be the lists there.
**Adriel Perkins** 12:21 Cool.
And then what I should be able to do is create a task list.
And then I'll just open up the first one into Python.
And… How do I… let's see, I wonder if it has to be created… As an issue first.
For it to issue on specification… And then I bet… yeah, so I have to convert this to a… Issue.
**Christophe Kamphaus** 13:22 I didn't know it.
**Adriel Perkins** 13:23 Bye.
**Christophe Kamphaus** 13:25 No, it is an issue.
**Adriel Perkins** 13:27 under specification…
**Christophe Kamphaus** 13:31 And can you move it to the other one?
**Adriel Perkins** 13:38 Not Premier.
**Christophe Kamphaus** 13:41 Can you move it with that?
No, doesn't look like it.
**Adriel Perkins** 13:49 Correct.
I don't have any ad, chain… yeah, hmm… I might have to get an admin… I might have to get Carlos. I'll ask Carlos to see if he can move this to a repo.
And then I won't add any other ones until we can figure out how to move them.
Worst case comes to worst case, we could also just, like, convert to sub-issue.
And then, a link.
do a, just a linking, but I'm gonna see if we can move it, because I feel like we should be able to move it.
So I'll put that ask out to Carlos to see if we can move it and then update accordingly.
**Christophe Kamphaus** 14:31 Sounds good.
Yes, no one else will join today.
**Adriel Perkins** 14:39 I think that's correct Is there anything you wanted to talk about?
**Christophe Kamphaus** 14:45 No, I'm pretty busy on my job right now.
And for the long-running tracers, that one, carlos will take… Okay.
**Adriel Perkins** 15:01 Maybe I should make this in progress?
**Christophe Kamphaus** 15:03 Maybe when he says he's working on it.
Okay. Maybe you can put it on to-do, since we will actually do it.
And from my side, when I have some capacity, I will, take a look at Jenkins.
If it's already implementing the specs as we… the semantic convention as we… Define some, otherwise I will propose some PRs for some.
**Adriel Perkins** 15:32 Okay, sounds great.
Appreciate it. Appreciate the work here.
I guess, we'll call it now, and… Yup. Give you some time back to your day.
**Christophe Kamphaus** 15:46 See you.
**Adriel Perkins** 15:47 Take care.
