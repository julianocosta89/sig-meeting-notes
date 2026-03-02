SIG: System Sem Conv Stability WG
Date: 2025-08-28
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/P4frS36Lgvqe_Sg6fWimtH9_zq82Wbw5_91BT54lqqJl1YP4oXdinMP40U1QESaA.9UmYdppFeMdf36st
============================================================

## Zoom Recording Transcript

**Christos Markou** 03:51 Hey there.
**Pablo Baeyens** 04:52 Should we start?
Do we have anything on the agenda?
look like.
**Christos Markou** 05:10 I'll go check the board, maybe, or, … Oh, Quicken.
**Pablo Baeyens** 05:17 Yeah, we Oh.
Somebody else share the screen? I have a pencil.
private tops, and….
**Roger Coll** 06:31 Well, I think last week we already had an overview, right, of the…
GA world, and we decided to
For KubeCon, just targeting the process area, right? And I think we…
We're quite fine there. There's just, … A few issues.
Left.
So, what would you like to go through? Maybe the GA board for the whole system, or anything specific?
**James Thompson** 07:14 For me, it's about the OS.
operating system… Attributes.
So… Yeah.
**Roger Coll** 07:23 Alright, it's… I think there's a PR for that, right?
**James Thompson** 07:27 C-correct, there's two PRs.
Which flows into a third.
**Roger Coll** 07:34 Wow.
**James Thompson** 07:38 It's… one of them's 2423.
**Roger Coll** 07:46 2, 4, 2, 3?
**James Thompson** 07:48 Yep.
**Roger Coll** 07:50 ….
**James Thompson** 08:06 And the one below.
**Roger Coll** 08:11 But… I think Bridon is not here, right? I think he had some… Some insights regarding this…
this PR, ….
**James Thompson** 08:26 So, I've got… so if you have a look at the diff…
Right? For the more… right, so the files change, you will actually see… so Brandon's feedback was about documenting what the expectation is for the different languages.
Alright, so if you go to the entities for OS.
**Roger Coll** 08:44 Paige?
Stitch one.
**James Thompson** 08:49 Right, and view the pretty version of that.
**Roger Coll** 08:55 Check.
**James Thompson** 09:01 Right?
So if you scroll down to the notes section, I've actually gone through for…
the key OSes on how to get that information.
Alright, so… The variant name, where that comes from, etc.
Alright, that was all was missing before Brandon's feedback.
**Roger Coll** 09:24 Okay.
**James Thompson** 09:25 Alright, so… yeah.
today, based on… like, I haven't filled in macOS, because I don't have access to a macOS, so I don't know…
what the equivalents for some of them for macOS would be.
Weather.
whether there is even an equivalent on Mac, I don't know.
But I've done… Linux is there, Windows is there.
**Roger Coll** 09:48 Oh, right.
So, well, for myself, I don't have the context of SPR, but basically, it's extending, I guess, the OS
attributes, I'm seeing, okay, and including this new variant.id, variant.name.
**James Thompson** 10:06 Okay.
**Roger Coll** 10:07 Okay.
**James Thompson** 10:09 Alright, so it's extending it based on what's already available in Elastic Common Schema, and it's gone to explain where that information can come from.
**Roger Coll** 10:19 Okay, I see.
Okay, it looks… good. I… I… for myself, I guess I will…
market to take a look. I think that…
maybe it's the other one that it's a bit more… there's a bit more discussion, I think, on the right SPR, about the Unix, etc.
**James Thompson** 10:44 Yep.
**Roger Coll** 10:45 Okay.
**James Thompson** 10:46 Alright, so… yeah. So, I think the more OS properties is pretty straightforward.
Right? Because I've gone through documenting where each of the properties can come from, etc.
**Roger Coll** 10:58 Okay.
**James Thompson** 10:59 Right.
**Roger Coll** 10:59 Yeah, looks quite… looks quite good at first glance.
Let's see if we can get also some help from the macOS, if someone has some knowledge there, and…
Should be fine.
**James Thompson** 11:13 Yep.
**Roger Coll** 11:14 Thank you.
**James Thompson** 11:15 And… but then the refocus OS.
**Roger Coll** 11:17 ….
**James Thompson** 11:18 Right.
So… Currently, we have OS type, which is…
a mismatch of types of OSes. Like, sometimes it's… if we look at the list, there's
Linux, sometimes… and if we look at Elastic, there's Unix, there's WatchOS, it's all over the place with
Different tiers of operating system types.
Alright, so… what I originally proposed was to go through and extend that list out to list all the different types of OS, watch OS, etc.
Then the feedback was, we should reduce it just to…
the basic ones from the OS.
Alright, based on the SDKs available.
Right? So what I've done…
is I've gone through the Java.NET, RAST, Python, etc. libraries to see what libraries they provide.
And the two most common ones they provide is Windows and Unix as the OS type enum.
Right? They have a… they usually have an additional attribute to get the OS name.
But they usually provide that split on the two.
Okay?
So… Right, so that… and that was with what was suggested in the Simcov, just to have those two.
**Roger Coll** 12:40 Huh.
**James Thompson** 12:41 Alright, so what I've done is I've reduced it down to just those two.
But, as you can see, there's been feedback about
removing that split for Darwin, FreeBSD, etc.
So, I agree, it's useful to have that split, but I'm mindful of
implementing this, how to get that information. So… what I…
have done is I've kept it to just the 2.
Unix and Windows here.
But, there is a third PR, which is linked in the description to this.
Right? Which introduces the Unix kernel namespace.
where you can capture, is it Darwin?
Alright, is it free BSD? And it actually describes how to get the kernel information.
Because the problem we have at the moment
Is we can't do os.kernel.name, because
Elastic Common Schema can't migrate to that.
Right, so… I think… If we can keep OS,
simple, with just the two, right, in this PR?
based on what the SDKs provide.
But… supported by having the Unix kernel.
name face there, where we'll know, is it a DAON OS, is it freeBSD, etc. So you still have that granularity there.
**Christos Markou** 14:16 Are those used already by the collector?
**Pablo Baeyens** 14:20 I think they are, yeah.
I was going to ask, …
do you think the Unix value is useful for… like, what kind of use case… because I can see myself wanting to know
what, …
machines in my fleet are using Windows, are using macOS, are using Linux, but using Unix in general.
I cannot think of a case where I want to distinguish Unix versus non-unix. It's mostly the more specific, ….
**James Thompson** 14:55 But you… but you still have OS name to get more specific, so that way, you know, is it a… is it a Red Hat machine? Is it your boom to… you have all that detail.
**Pablo Baeyens** 15:06 Sure, yeah.
No, I'm not, I'm not saying, like, you cannot…
get that information with the alternative we're proposing. It's more about
Is this attribute useful after, … Like, the… the change.
**James Thompson** 15:25 I see it as limited, but…
it's a field that's brought across from Elastic as well.
And Elastic has both… Elastic has both Unix and Windows defined as values.
As well.
**Pablo Baeyens** 15:41 Huh?
Yay, I guess… maybe having someone from Elastic that is knowledgeable about that and can tell us, like.
how… has it been useful for their users? That, I think, would be very useful for this conversation. Like, if we can find somebody, I don't know.
Christus or Roger, if you know somebody.
**Roger Coll** 16:03 you can…
Yeah, we can ask internally, but I… I think I agree with Pablo's comment. I'm not sure in…
I don't have in my mind any case that I would, I don't know, filter a dashboard by… by Unix, or… and… and differentiate Darwin from…
you know, let's say put Linux and Darwin in the same
place instead, and comparing it to Windows, for example, right? So, in that sense, I… I feel that then it sh…
the valuable attribute, it would be the OS name, right?
I know.
and not always type. That's, I guess the…
the root cause of the concerns about… about kind of renaming or moving these… these values, but… but we can ask, yeah.
**James Thompson** 16:54 But what I think we can do is, like.
If we improve the messaging, saying, If… if you're using… Mike.
the Unix kernel stuff.
More… required, for example.
Alright, saying, conditionally required. If OS type is Unix, then you should also provide the Unix kernel type.
For example.
**Roger Coll** 17:22 Right. Yeah, but then you increase the cardinality, right?
With actually, let's say, … getting too much value from OS.type.
But, well.
**James Thompson** 17:37 Has it….
**Roger Coll** 17:38 Yeah.
**James Thompson** 17:38 as it currently stands, OSUP type is only used for…
in the resources, resource, alright, the entities and the resource detectors. It's not actually referenced in any metrics.
Yeah.
**Roger Coll** 18:03 Yeah, I'm not sure. I guess maybe we need to get more.
I don't know, more feedback from folks, and…
And, yeah, yeah, yeah, someone, I don't know, would find valuable this, ….
**James Thompson** 18:17 Yeah, it's just for me, the values didn't seem very consistent.
**Roger Coll** 18:23 Yeah, yeah, I guess.
**Pablo Baeyens** 18:26 Right, I guess there's a trade-off here between, like, being… More faithful to the…
thing that you are representing, or being more useful, sometimes being less faithful. I think it's the same conversation as with the Windows thing. It's true that it's… Windows refers to Windows NT, and that there's historical,
Historically, there's other kernel versions of Windows, but today, most people, like, identify Windows with Windows NT kernel, so…
I feel like it's a similar situation, but I agree with Roger, like, we can… we can see, we can get more feedback, and, like, maybe, yeah, if we… if this has been used elsewhere, if this has been used in Elastic, and we have some… some feedback from them, like, this was useful, this was not useful, that would be a way to… to set up.
**James Thompson** 19:18 Yeah. Like, in Elastic, they have Unix, they have Windows, they have Linux, they have WatchOS listed.
And… You look at it, and it's a total mismatch.
Alright.
Alright.
Because, technically, WatchOS,
Right? It could be described as a Linux OS or a Darwin OS, but it could also be described as Unix.
Alright, so… And for me, it was also about how would this be implemented?
Consistently across languages, which is where it gets tricky.
Yeah, that's a very fine, ….
**Roger Coll** 19:58 I guess… Yeah, it's about improving the ECSG schema, for sure there's…
Yeah, misalignments there, so, yeah, that's better, so… Place for… for improvement.
Okay, cool, I will note it, and I will ask.
to see if someone internally in Elastic has been using this OS type for dashboards, or… Or whatever, but…
And yeah, and unshare the feedback back.
But yeah, the downside of, …
let's say, then relying on, for example, the unix.kernel.name, let's say this additional conditional… Is that, …
You know, there's sometimes some backends that, …
cannot easily, you know, create queries or conditionals on attributes that, for example, do not exist, right? And you rely on, for example, always having the os.type.
And…
And that's fine, and you have all the information there. But in that case, you would need then to assert that this attribute, for example, it's not null , and then assert the value.
And so it complicates a little bit more the…
the… the queries for… just wanted to differentiate, let's say, the OS name, or… or OS type, but…
Yeah, let's…
I don't know, let's keep it the discussion in this… in this issue, and as I said, I… I will…
I will try to ask in Elastic if there's been any use case for Unix and Windows.
But yeah, thanks for… for all this.
putting this together, I think it's…
It's nice that we are… yeah.
getting all the different pieces, and at least unifying all the OS's name, and have all this clear.
And I think this can, I guess, this Unix…
namespace can still… it's independent, right, from this OS PR, so this still can make it. So that's… that's great, thank you.
All right.
**Pablo Baeyens** 22:38 In terms of the…
the GA board, there's no… there's been no progress, right? It's just, like, we… we are at the same state that we were last week. We want to focus on process, but….
**Roger Coll** 22:51 Yeah, correct.
**Pablo Baeyens** 22:53 Okay.
**Roger Coll** 22:54 Much progress.
Let's see, bye next week.
**Pablo Baeyens** 23:01 Right?
**Roger Coll** 23:03 So….
**James Thompson** 23:04 Can we look at 2673?
**Roger Coll** 23:12 2….
**James Thompson** 23:13 673 here.
**Roger Coll** 23:15 3. Yep.
**James Thompson** 23:24 Yeah, so this ties into the process.
Alright, because you mentioned….
Yeah.
Right, so… Yeah.
**Roger Coll** 23:41 Yeah, I will take a look, and this is…
My main concern about that one is that, is this always available? …
the executable version, because I think profiling what it does
it… it uses, like, … well, they created a random algorithm, and they do the… the diggers, right? Then they get the latest bytes, or something like that, and that's kind of the ID that they use for the executable version, or build ID.
Are we talking about the same here, or it's a different one?
Alright.
**James Thompson** 24:20 It's… Yeah.
Right, it's about having a generic process executable ID. Version ID.
Right.
Because if you look at… what was the other ones? And I did one up here… It was…
2657.
**Roger Coll** 25:01 Okay.
**James Thompson** 25:03 Alright, so this creates an entity for the process executable.
**Roger Coll** 25:08 Yeah.
**James Thompson** 25:10 Alright.
**Roger Coll** 25:10 This is for profiles, right?
**James Thompson** 25:13 No, it's gen… foreign in general.
**Roger Coll** 25:16 In gen… okay, but… Can you have metrics for a processor? Well, maybe, yes, okay.
Yeah, yeah,
**James Thompson** 25:28 Alright.
**Roger Coll** 25:29 Yeah, but so when I was doing this.
**James Thompson** 25:31 the question from Josh came up, right? Alright, can you…
First, all the roles for the entity, right? And that's where…
Alright, the discussion about the version that came in.
**Roger Coll** 25:48 Huh.
**James Thompson** 25:49 Right? Because if we don't have a generic version for the process.
Alright, executable, that means we will always have Just the one.
Process Executable entity.
Whereas if we add a version there, we can actually have separate entities, so when you update it, you can see… have a separate entity.
Yes, so this is a summary from Josh.
**Roger Coll** 26:21 Okay, hmm.
**James Thompson** 26:22 Yeah, and so that's… that's what caused the introduction of the SIP Separate process executable version attribute.
Yeah.
**Roger Coll** 26:37 Okay, I will take a look, but yeah, probably the profiling maintainers might…
Have more knowledge on that area, probably.
**James Thompson** 26:49 Yeah, it's a secret. So, like, the profiling version ID's still there.
**Roger Coll** 26:55 Okay.
It's more on the entity side.
**James Thompson** 27:01 Yeah, the entities and the resource detector.
Yeah.
**Roger Coll** 27:05 Okay, I will… I will give a tip, that's all. Thank you.
Okay, I will put those PRs on the document, in case anyone else wants to…
Take a look. Thanks for sharing it, James.
Alright, let's recalling it a knitting, or anyone else has something to share?
Okay.
**Christos Markou** 27:50 We're okay.
**Pablo Baeyens** 27:52 Yep.
**Roger Coll** 27:53 Sounds good, then.
**Christos Markou** 27:55 Thank you, Ron. See you next week.
**Roger Coll** 27:56 Thank you.
**James Thompson** 27:57 Alright.
**Pablo Baeyens** 27:57 Thank you.
**Christos Markou** 27:58 Bye.
