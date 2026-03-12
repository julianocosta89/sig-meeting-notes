SIG: Agent Management WG
Date: 2026-02-03
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/pjsDLo3ZiI7TvZwPjVPuQ9TO0nZmsVrVKFnY-hh8ovDeH3w4pTvXSa2rDJBfFiMS.h_LQNG5sDRw32LhL
============================================================

## Zoom Recording Transcript

**Douglas Camata** 00:24 Hello?
**Tigran Najaryan** 00:28 Hello.
If you have topics to discuss, please add to the agenda. I'm posting the link to the document.
Okay, I think we should start. There's only one thing I see there, the supervisor roadmap conversation. I think the expectation was that Antoine is going to start the discussion, open it up. I don't know if anything happened. I'm not aware of that.
And I don't see him here.
So… I… we haven't made… at least I'm not aware of any progress made since last time.
**Douglas Camata** 02:28 Yeah, I don't…
**Tigran Najaryan** 02:28 I don't know if anybody knows.
**Douglas Camata** 02:29 don't… I don't know as well if… The idea was to talk about it in the collector's SIG. I guess it was… To talk about it here, but if, if not today.
No problem, and I was just curious to know if we have a planned date for a conversation, or if we would just do No, next time that we are able to get everyone.
**Tigran Najaryan** 02:57 In the last hole.
two weeks ago. I think we left the call with… when I asked Antoine to organize the discussion, I think that that's where we left.
If he did anything, I'm not aware of that.
But… we need somebody to drive that, and I think he said either he or Someone from his… PM's team is going to help with that.
I don't know if anything happened. I can ping him to see, what's going on there, if we can make progress on that.
Adam, do you know, maybe, if any discussions happened in the collector's seat, maybe?
**Evan Bradley** 03:37 Nothing has happened. He called out, was it Anch? I don't… there's somebody that is from Splunk. I've seen this person around before that, he said was going to help.
**Tigran Najaryan** 03:51 Okay, I'll ping on that.
**Evan Bradley** 03:52 op-amp sync meeting.
**Tigran Najaryan** 03:54 Yeah, yeah. I'll ask him whether he still intends to… help organizing those discussions. If not, I guess we can still do that on our own.
But it would help if… Someone who knows how to do these things helps us. They are… they are product managers. They do roadmaps all day, so… our thinking.
**Douglas Camata** 04:17 Yeah, I think also more than, than, than timelines, I think it will be more a discussion about… What kind of features… that we want to add to the supervisor, given some goals that it has, like, being stable, being very reliable, as simple as possible, right? I think,
**Tigran Najaryan** 04:42 Think dead.
**Douglas Camata** 04:43 For that, of course, PMs can contribute, but I don't think they are required, because I don't think we will need to discuss, like, timelines.
But that would be cool as well, if we can, of course.
**Tigran Najaryan** 04:59 Yeah, yeah, we can absolutely do it on our own. It just helps if we're a bit more systematic about it. One thing I would expect the PMs to do, for example, is to go over the existing open issues and see if there's anything that should lend into our At least the inbox of what we want to review and consider for the roadmap.
So, sure, we can do it, but I personally don't really have time to do it myself at the moment, right? So it's work that needs to be done.
since he subscribed to do it, I was hoping that he can do it. I'll ping him, let's see how that goes. But… If he doesn't, then I agree, we should still go ahead and do… maybe self-organize a bit and make sure it happens.
**Douglas Camata** 05:45 Yeah, yeah, yeah, of course, yeah, we can give him some time as well, he doesn't, that's not…
**Tigran Najaryan** 05:51 Ping him, we work kind of almost in the same team, so I'll ping him to see where he is.
**Douglas Camata** 05:58 Yeah, yeah, I have some interest in that because, I… there… Because, of course, of the work on the initial fallback configuration, the feature that changed name a little bit, and I have I have a follow-up for that in mind already.
And I want to see how that could fit in this possible roadmap.
Which is, basically, I would like to… use the comp map from the collector in the supervisor, so that I could pull this initial fallback configuration from S3, for example. But, well, when the discussion comes, I will… I will bring this point as well.
**Tigran Najaryan** 06:47 You should also feel free to open issues with thoughts you have, ideas and proposals.
I think we should definitely look at whatever open issues we have as an input to those discussions. So, anybody who has any thoughts on what they would like to see in the roadmap, you can… you can do the same thing, and we'll make sure to, at the very least, take into account those things. We're obviously not going to do all the things that are proposed, but that will be an input for us.
**Douglas Camata** 07:21 Yeah, yeah, sounds good. Thank you.
**Tigran Najaryan** 07:25 Okay.
So, I… I suggest we, again, we… We'll leave this out for now, and then we'll see whether we can make any progress before the next call.
Okay, let's move on the demo stuff. Johani, do you want to talk about it?
**JM Juande Manjon** 07:48 Yeah, so, yeah, start working on the open server integration with the… with the demo. Lose fine, so basically what I had done is copied the whole example into a SUF folder in the… in the hotel demo.
I have to rename the package name, because we're using internal.
That's the point to keep on.
**Tigran Najaryan** 08:10 Sorry, one quick question before you do all the hard work, I guess. Have you… talked to the demo folks, whether they are interested in having that in Autel Demo.
**JM Juande Manjon** 08:22 I have… I have planned to be in them tomorrow. I think tomorrow they have the SEEK meeting.
**Tigran Najaryan** 08:26 Yeah, yeah. Make sure you do that, because they may also say they don't think it's the right place. I don't want you to spend too much time on an approach that is a dead end.
**JM Juande Manjon** 08:37 Yeah, so I… okay, so that date is very short, so I copy and renamed the… the model names to remove the keyword.
LinkedIn or keyword.
that doesn't allow, to compile the server, I just… integrated, and it… the Docker Compose works.
So I can see the Pan server running.
I had some issues with the front, proxy, because the… the way that I implement the proxy is to be able to access to the UI.
But at least I see the Open server running.
So it was, not too much effort, so I'm gonna follow up with them.
After having the okay with the hotel demo.
Maintenance, I will move forward and try to implement the supervisor Image to be able to have… to be able to… to modify the… The settings on the collector's be a supervisor.
And the third step will be supporting Kubernetes, but one step One thing.
So this is on my update. So, the main thing is… For me, it's not okay duplicating the whole code, but this is the way to go.
**Tigran Najaryan** 09:57 I think that's one of the things that we'll need to figure out. Do we keep both this, I guess, the limited demo that we have in OpampGo, and then you go, I guess, and create a more sophisticated one in the demo repository?
Or… we get rid of the… this one when the… when the auto demo version is there, and it shows everything that is possible to do. I'm not sure what's the right answer here.
But we'll need to figure it out. Maybe it's okay to have both, I guess, if they are… Targeted at different audiences, maybe, so we'll need to see.
**JM Juande Manjon** 10:35 So, in my personal opinion, I think it's having… OpenGo Contrib would be the solution where we have one place, to have all the contribution to the… and tools to the OPAN, protocol, and using that OpenGo country as input for the demo.
**Tigran Najaryan** 10:59 Possibly. I guess in that case, we'll need to find the right set of maintainers for that new repository. We need at least two people.
To be maintainers, so that we can create a repository.
It's a possibility, what you're suggesting. Let's do this, let's, let's first… understand whether it's going to be in Hotel Demo, whether the Hotel Demo SIG wants it in the demo.
And we can take it from there, because if they don't, then we'll need to… I guess we'll go back to the drawing board, essentially, to understand where do we put it.
**JM Juande Manjon** 11:38 I believe that the one community will like to have the supervisor and OpenServer integrated with the demo.
**Tigran Najaryan** 11:45 I agree with you. I think a demo, yes. It would be good to have it in a demo, yes.
**JM Juande Manjon** 11:52 Yeah, so I will let you know, guys, in the next meeting.
**Tigran Najaryan** 11:57 I'm good, thank you. Thanks for working on this.
Okay, that's all in the agenda. Anything else, anyone?
Ange, you're here. You joined. So, we're just trying to understand if there is… there has been any progress on the… On the roadmap issue, did you talk to Antoine about doing the roadmap for the supervisor for OPAM?
**Aunsh Chaudhari** 12:36 Yes, yes, I was unfortunately, yeah, running over from another customer call, so we had a brief discussion, and I did want to, bring this up as a call to action, or just call an ask of collaborating along. I have a rough draft that I'm putting together, and I'd love to share. Let me just get to the… Well, temp.
SIG doc. Give me a minute.
Great, yeah, absolutely. Evan, I will add you.
Let me find this here.
Great. Can… I've just added that to the, document, and, I can share my screen as well.
For folks I haven't met before, I'm currently… basically on the product team at Splunk Observability, and I'm definitely a lot interested into OPAMP and agent management at a high level. I've discussed this with Antoine as well, and I've been Looking into more detail, learning a little bit more, and understanding all of the different use cases around the op-amp extension and supervisor.
My goal here was, as you walk through this, again, a very high-level draft of my understanding so far around, from a product or an outcome-driven view that customers have from the supervisor, what Other jobs to be done for the supervisor at the moment.
And, more or less, I think we want to evaluate what is not the supervisor's job, right? What is out of scope?
The set of guiding principles that we should think through as we move forward.
And, also starting off with the roadmap. Again, this is very much a skeletal talk at this point, right? I'm diving more deeper, and this is where I'd love to collaborate with Evan, as he mentioned, and any other folks who are interested, right, who'd… Who've obviously been deeply involved in the project so far, but also are interested in seeing where this moves forward, right, in terms of the roadmap, so… Yeah, feel free to, again, add comments. As I mentioned, it's a draft, but if there are any top-level questions, perspectives that you'd like to see this doc evolve into? I think I'd be happy to hear those from the group.
**Tigran Najaryan** 15:41 This is great. Thanks, Ash, for doing it. I will… I will review it probably offline. I… I'm not sure we have… want to have, like, a live, detailed review right now. We could, I guess, if there is an interest, but I personally would like to take a bit of time and do it offline.
One thing I wanted to ask you, if you haven't already done it, can you take a look at what open issues we have about the supervisor in the collector repository, and maybe see if that… if there's anything that Looks like it's a reasonable… Proposal that could or could not be maybe added to the… to the roadmap, so that sort of, we can have a discussion around that, whether it's something that fits or doesn't fit the roadmap. Essentially, use the open issues as another input for the roadmap.
**Aunsh Chaudhari** 16:31 Yeah, absolutely. I did take a look at a few, and I'll be also reviewing some of the current state of the things that have been completed out of the spec, right? So, I'll definitely review those, and that'll be an important point to consider here. Sounds good, yeah.
**Tigran Najaryan** 16:46 Okay, okay, great, thanks.
Okay, I'll personally take a look offline, if anybody wants to maybe have a discussion here, feel free.
That's fine as well.
By the way, I think it's… I opened the doc, it's read-only. Did you… Did you give, maybe commenting access, I guess, would be useful, right?
**Aunsh Chaudhari** 17:18 Yep, thank you.
**Tigran Najaryan** 17:19 Not necessarily direct editing, but if you can allow commenting, that would be useful.
**Aunsh Chaudhari** 17:24 Yes.
That's work.
Let me do that, yeah.
Yeah, it's done.
**Tigran Najaryan** 17:38 Thank you.
**Aunsh Chaudhari** 17:47 Great.
**Tigran Najaryan** 17:51 Okay, so unless anybody wants to have any… any other… any live discussion of this, I guess we can maybe end here, and you guys feel free to take a look at the doc, comment on it.
Give your input.
And hopefully by the next call.
We'll have a bit more to discuss.
**Aunsh Chaudhari** 18:14 Sounds cool.
**Tigran Najaryan** 18:19 Okay.
I think that's all for today.
Thank you all.
**Aunsh Chaudhari** 18:26 Thank you.
**Douglas Camata** 18:26 go by.
